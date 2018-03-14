#-*- encoding:utf-8 -*- 
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required 
from catalogue.models import Agency
from customer.models import Reservation
from django.contrib.auth import login , authenticate , logout 
from catalogue.models import Country
from django.db import IntegrityError 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages
from customer.forms import ReservationForm
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import Group
from catalogue.models import Package
import datetime 
"""
retail customer views
"""

@login_required
def profile(request):
    # we will not be pessimistic and will assume the user is not registered 
    if not request.user.is_authenticated() : 
        return redirect('customer:register_customer')

    # print Reservation.objects.filter(user=request.user).delete()
    if not Reservation.objects.filter(user=request.user , is_canceled = False ).exists() and request.session.get('is_pending') == 'True':
        data = {}
        for key , value in request.session.items() : 
            data[key] = value 

        form  = ReservationForm(data = data ) 
        if form.is_valid(): 
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save() 
            
            del request.session['is_pending']
    try : 
        reservation = Reservation.objects.get(user = request.user , is_canceled = False )
    except ObjectDoesNotExist : 
        reservation = None

    return render(request , 'profile.html' , {'reservation' : reservation} )

def reservation(request, package_id):
    package = Package.objects.get(id = package_id)
    if request.method == 'POST' :
        form = ReservationForm(request.POST)
        """
        save all variables as session variables
        :: if needed :: exclude theses default session varibales when deleting in profile view 
        [(u'_auth_user_hash', u'ed93fd3a13d66bb6d7fcee07ec35abfc5ec7d21d'), 
        (u'_auth_user_id', u'14'), 
        (u'_auth_user_backend', u'django.contrib.auth.backends.ModelBackend')]
        """
        if form.is_valid():
            POST = request.POST.dict()
            for key , value in POST.items() : 
                request.session[key] = value
            request.session['is_pending'] = 'True'
        return redirect('customer:profile')

    return render(request , 'reservation.html' , {'package' : package , 'some_date' : datetime.date.today() })

def cancel_reservation(request , reservation_id):
    res = Reservation.objects.get(id =reservation_id)
    res.is_canceled = True
    res.save()
    print res
    print res.id 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def change_phone_number(request , reservation_id):
    if request.method == 'POST':
        res = Reservation.objects.get(id =reservation_id)
        res.phone_number = request.POST.get('phone_number')
        res.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponse(status = 404 )
"""
Authentication views 
"""

def register_user(request):
    group_name = request.POST.get('group_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    title = request.POST.get('title') 
    country_id = request.POST.get('country_id')
    phone_number = request.POST.get('phone_number')

    try : 
        user = User.objects.create(
            username = username 
            )
    except IntegrityError : 
        messages.add_message(request , messages.INFO  , 'يوجد حساب بنفس اسم المستخدم')
        return None , None 

    # assign a group 
    group , created = Group.objects.get_or_create(name = group_name)
    user.groups.add(group)

    # set password
    user.set_password(password)
    user.save()

    user = authenticate(username= username, password = password )

    login(request ,user)
    if group_name == 'agency' : 
        # create agency 
        agency = Agency.objects.create(
            created_by = user, 
            title = title ,
            country_id = country_id ,  
            phone_number = phone_number
         )
    else: 
        agency = None 

    return user , agency

def register_agency(request):
    if request.method == 'POST' : 
        user , agency = register_user(request)
        if not user : 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return redirect('supplier:agency' , agency_id= agency.id)

    context = {}
    context['countries'] = Country.objects.all() 
    return render(request , 'register_agency.html' , context)


def register_customer(request):
    if request.method == 'POST' : 
        user , agency = register_user(request)
        if not user : 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return redirect('customer:profile') 

    return render(request , 'register_customer.html')


def authenticate_user(request):
    username  = request.POST.get('username') 
    password        = request.POST.get('password') 

    if username and password : 
        user = authenticate(username=username, password=password)
    else: 
        user = None 

    return user 

def login_agency(request):
    if request.user.is_authenticated(): 

        if request.user.groups.filter(name="agency").exists() : 
            # return request.user
            agency = Agency.objects.get(created_by = request.user)
            return redirect('supplier:agency' , agency_id = agency.id)

        else : 
            return HttpResponse(status = 404)


    if request.method == "POST":
        user = authenticate_user(request)

        if user : 
            if not user.groups.filter(name="agency").exists():
                return HttpResponse(status = 404 ) 

            login(request, user)
            agency = Agency.objects.get(created_by = user)
            return redirect('supplier:agency' , agency_id = agency.id)

    return render(request , 'login_agency.html'  ) 

def login_customer(request):
    if request.user.is_authenticated(): 

        if request.user.groups.filter(name="retail").exists() : 
            return redirect('customer:profile')

        else : 
            return HttpResponse(status = 404)


    if request.method == "POST":
        user = authenticate_user(request)

        if user : 
            if not user.groups.filter(name="retail").exists():
                return HttpResponse(status = 404 ) 

            login(request, user)
            return redirect('customer:profile')

        else : 
            return HttpResponseRedirect
    return render(request , 'login_customer.html'  ) 


@login_required 
def logout_user(request):
    logout(request) 
    return redirect(request.META.get('HTTP_REFERER'))


