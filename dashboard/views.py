#-*- encoding:utf-8 -*- 
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate , logout , login
from django.contrib.auth.models import User
from django.db import IntegrityError 
from catalogue.models import Package  , Agency 
from django.http import HttpResponse
from dashboard.forms import PackageForm
from .forms import AgencyForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@login_required() 
def dashboard(request):
    context= {} 
    packages = Package.objects.filter(user = request.user ) 
    context['packages'] = packages 
    try : 
        agency =  Agency.objects.get(user = request.user ) 
    except ObjectDoesNotExist : 
        agency = None 

    if request.method == 'POST':
        agency , r = Agency.objects.get_or_create(user = request.user ) 

        form = AgencyForm(request.POST, instance = agency ) 
        if form.is_valid() : 
            form.save()
            messages.add_message(request , messages.INFO , 'تم تحديث معلومات الشركة بنجاح')
        else: 
            context['form_errors'] = form.errors

    context['agency'] = agency 
    return render(request , 'dashboard.html' , context )

def dashboard_package(request):
    if request.method == 'POST' : 
        form = PackageForm(request.POST)

        if form.is_valid():
            instance = form.save(commit = False ) 
            instance.user = request.user 
            instance.save()
            messages.add_message(request , messages.INFO , 'تمت اضافة عرض العمرة بنجاح ')

            return redirect('dashboard')

    return render(request , 'package_form.html' )

@login_required
def remove_package(request, package_id):
    package = Package.objects.get(id = package_id ) 
    if package.user == request.user : 
        package.delete()
        messages.add_message(request , messages.INFO , 'تم حذف العرض')
        return redirect(request.META.get('HTTP_REFERER'))

    return HttpResponse(status =404 )
"""
Authentication views 
"""

def register_user(request):
    if request.method == 'POST' : 
        username = request.POST.get('username')
        password = request.POST.get('password')
        try : 
            user = User.objects.create(
                username = username 
                )
        except IntegrityError : 
            messages.add_message(request , messages.INFO  , 'يوجد حساب بنفس اسم المستخدم' )
            return redirect(request.META.get('HTTP_REFERER'))

        user.set_password(password)
        user.save() 

        user = authenticate(username= username, password = password )
        login(request ,user)

        return redirect('dashboard') 
        
    return render(request , 'register.html' )

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
            return redirect('dashboard')

        else : 
            messages.add_message(request , messages.INFO  , 'اسم المستخدم وكلمة المرور ﻻ يتطابقان' )

        
        # else : 
			# messages.add_message(request , messages.INFO ,  ''  ) 

    return render(request , 'login.html'  ) 



@login_required 
def logout_user(request):
    logout(request) 
    return redirect(request.META.get('HTTP_REFERER'))
