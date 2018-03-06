#-*- encoding:utf-8 -*- 
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required 
from catalogue.models import Photoshot , MakkahHotel , MadinahHotel , Agency
from django.contrib.auth import login , authenticate , logout 
from catalogue.models import Country
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages
@login_required
def profile(request):
	# default session varibales 
	# [(u'_auth_user_hash', u'ed93fd3a13d66bb6d7fcee07ec35abfc5ec7d21d'), 
	# (u'_auth_user_id', u'14'), 
	# (u'_auth_user_backend', u'django.contrib.auth.backends.ModelBackend')]
	if request.session.get('pending_reservation'):
		print 'fdsfdas'	

	return render(request , 'profile.html'  )

def reservation(request):
    context = {}
    context['photos'] = Photoshot.objects.all()[:5]
    context['range_list'] = range(10)
    return render(request , 'reservation.html' , context )


"""
Authentication views 
"""
def register_user(request):
    if request.method == 'POST' : 
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
            messages.add_message(request , messages.INFO  , 'يوجد حساب بنفس اسم المستخدم' )
            return redirect(request.META.get('HTTP_REFERER'))

        user.set_password(password)
        user.save()

        # create agency 
        agency = Agency.objects.create(
            created_by = user, 
            title = title ,
            country_id = country_id ,  
            phone_number = phone_number
         )
        
        user = authenticate(username= username, password = password )
        login(request ,user)
        
        return redirect('agency' , agency_id= agency.id) 
        
    context = {}
    context['countries'] = Country.objects.all() 

    return render(request , 'register.html' , context)

def login_user(request): 

    if request.method == "POST":
        username  = request.POST.get('username') 
        password        = request.POST.get('password') 

        if username and password : 
            user = authenticate(username=username, password=password)
        else: 
            user = None 

        if user : 
            login(request, user)
            agency = Agency.objects.get(created_by = user)
            return redirect('supplier:agency' , agency_id = agency.id)

        else : 
            messages.add_message(request , messages.INFO  , 'اسم المستخدم وكلمة المرور ﻻ يتطابقان' )

    return render(request , 'login.html'  ) 



@login_required 
def logout_user(request):
    logout(request) 
    return redirect(request.META.get('HTTP_REFERER'))


