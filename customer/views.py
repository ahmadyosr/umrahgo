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
    # print Reservation.objects.filter(user=request.user).delete()
    does_reservation_exists =  Reservation.objects.filter(user=request.user , is_canceled = False ).exists()
    reservation_is_pending = request.session.get('is_pending') == 'True'

    if reservation_is_pending : 
        if not does_reservation_exists: 
            data = {}
            for key , value in request.session.items() : 
                data[key] = value 

            form  = ReservationForm(data = data ) 

            if form.is_valid():
                instance = form.save(commit = False)
                instance.user = request.user
                instance.save()
                del request.session['is_pending']

        elif does_reservation_exists : 
            messages.add_message(request , messages.INFO , 'يوجد حجز قيد التنفيذ ، الرجاء الغاء الحجز قبل إنشاء حجز آخر .')

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

            package = Package.objects.get(id= request.session.get('package'))

            request.session['departure_cost'] = package.__dict__.get(request.session['room_size']) 

            request.session['room_size'] = request.session['room_size'].replace('_cost' ,'') # check resrervation.html to see why we did this replace
            request.session['is_pending'] = 'True'

        return redirect('customer:profile')

    return render(request , 'reservation.html' , {'package' : package , 'some_date' : datetime.date.today() })

def cancel_reservation(request , reservation_id):
    res = Reservation.objects.get(id =reservation_id)
    res.is_canceled = True
    res.save()
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

def login_user(request):
    request.session['group'] = 'retail' # this will be used in 'post_fb_auth' view

    if request.method == "POST":
        user = authenticate_user(request)

        if user : 
            login(request, user)

            if user.groups.filter(name="retail").exists():
                return redirect('customer:profile')

            elif user.groups.filter(name="supplier").exists():
                # return request.user
                agency = Agency.objects.get(created_by = request.user)
                return redirect('supplier:agency' , agency_id = agency.id)
        
        return HttpResponse(status = 404)
        
    return render(request , 'login_user.html'  ) 

def post_fb_auth(request):
    group_name = request.session.get('group')
    user = request.user

    if not user.groups.exists() and group_name :
        group ,created  = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

    return redirect('customer:profile')

@login_required 
def logout_user(request):
    logout(request) 
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_account(request):
    return HttpResponse(status =404)