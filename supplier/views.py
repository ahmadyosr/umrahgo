#-*- encoding:utf-8 -*- 
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate , logout , login
from django.contrib.auth.models import User
from django.db import IntegrityError 
from catalogue.models import Package  , Agency  , Photoshot , MakkahHotel , MadinahHotel
from django.http import HttpResponse
from supplier.forms import UpdatePackageForm , PackageForm , AgencyForm
from django.core.exceptions import ObjectDoesNotExist
from dashboard.views import migrate_prices 
# Create your views here.

@login_required() 
def agency(request , agency_id):
    context= {} 
    agency =  Agency.objects.get(id = agency_id )

    if request.method == 'POST':
        form = AgencyForm(request.POST, instance = agency ) 
        if form.is_valid() : 
            form.save()
            messages.add_message(request , messages.INFO , 'تم تحديث معلومات الشركة بنجاح')
        else: 
            context['form_errors'] = form.errors

    if request.user.is_staff  : 
        packages = Package.objects.filter(catalogue_agency = agency)
        context['matched_agencies'] = Agency.objects.filter(created_by__is_staff = False)
        
    else : 
        packages = Package.objects.filter(created_by = request.user).exclude(is_removed = True )
        return render(request , 'supplier/agency.html' , context )

    context['agency'] = agency 
    context['packages'] = packages 
    return render(request , 'dashboard/agency.html' , context )

def supplier_package(request):
    context={}
    agency_id = request.GET.get('agency_id')
    agency = Agency.objects.get(id = agency_id) 

    if request.method == 'POST' : 
        form = PackageForm(request.POST)

        if form.is_valid():
            instance = form.save(commit = False ) 
            instance.created_by = request.user 
            instance.is_created = True 

            if request.user.is_staff  : 
                instance.catalogue_agency = agency
                migrate_prices(instance)
            instance.save()
            messages.add_message(request , messages.INFO , 'تمت اضافة عرض العمرة بنجاح ')

            return redirect('supplier:agency' , agency_id = agency_id )

    context['agency'] = agency

    context['makkah_hotels'] = MakkahHotel.objects.all() 
    context['madinah_hotels'] = MadinahHotel.objects.all() 
    return render(request , 'package_form.html' , context )

@login_required
def remove_package(request, package_id):
    package = Package.objects.get(id = package_id ) 
    if package.created_by == request.user : 
        
        if request.user.is_staff : 
            package.delete() 
        else : 
            package.is_removed = True 
            package.save() 

        messages.add_message(request , messages.INFO , 'تم حذف العرض')
        return redirect(request.META.get('HTTP_REFERER'))

    return HttpResponse(status =404 )

@login_required
def update_package(request, package_id):
    package = Package.objects.get(id = package_id ) 

    if (package.created_by == request.user or request.user.is_staff ) and request.method == 'POST' :
        form = UpdatePackageForm(request.POST , instance = package)
        
        if form.is_valid() :
            instance = form.save(commit = False )
            if request.user.is_staff :
                migrate_prices(instance)

            if not instance.is_created : 
                instance.is_updated = True 

            instance.save()
        else :
            return HttpResponse(status = 503) 

        messages.add_message(request , messages.INFO , 'تم تحديث العرض')
        return redirect(request.META.get('HTTP_REFERER'))

    return HttpResponse(status =404 )
