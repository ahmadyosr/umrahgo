#-*- encoding:utf-8 -*- 
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.db import IntegrityError 
# Create your views here.

@login_required() 
def dashboard(request):
    return render(request , 'dashboard.html')

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

        print '1' 
        if username and password : 
            user = authenticate(username=username, password=password)
        else: 
            user = None 

        print '2'

        if user : 
            login(request, user)
            return redirect('dashboard')

        else : 
            print 'OOOOOO MMMMMMMM GGGGGGGGG'
            messages.add_message(request , messages.INFO  , 'اسم المستخدم وكلمة المرور ﻻ يتطابقان' )

        print '3'
        
        # else : 
			# messages.add_message(request , messages.INFO ,  ''  ) 

    return render(request , 'login.html'  ) 


