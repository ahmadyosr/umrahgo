#-*- encoding:utf-8 -*- 
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate , logout , login
from django.contrib.auth.models import User
from django.db import IntegrityError 
from catalogue.models import Package  , Agency  , Photoshot , MakkahHotel , MadinahHotel , Date
from django.http import HttpResponse
from supplier.forms import UpdatePackageForm , PackageForm , AgencyForm
from django.core.exceptions import ObjectDoesNotExist
from dashboard.views import migrate_prices 
import datetime
# Create your views here.

@login_required
def agency_profile(request):
    if not request.user.groups.filter(name="supplier").exists():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {}
    agency = Agency.objects.get(created_by = request.user)
    packages = Package.objects.filter(created_by = request.user).exclude(is_removed = True )

    if request.method == 'POST':
        form = AgencyForm(request.POST, instance = agency ) 
        if form.is_valid() : 
            form.save()
            messages.add_message(request , messages.INFO , 'تم تحديث معلومات الشركة بنجاح')
        else: 
            context['form_errors'] = form.errors

    context['agency'] = agency
    context['packages'] = packages
    print agency.title

    return render(request , 'supplier/agency.html', context )      

@login_required 
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


def get_calendar(months_range):
    start = datetime.date.today().replace(day=1)
    one_day_delta = datetime.timedelta(days = 1) 
    dates = [] 

    start_month = start.month
    i = 0 ;
    while i < months_range:
        dates += [start] 
        start = start + one_day_delta

        if start_month != start.month :
            start_month = start.month
            i = i + 1

    return dates 
def supplier_package(request):
    
    context={}
    package_id = request.GET.get('package_id')

    if package_id : 
        package = Package.objects.get(id = package_id)
    else :
        package = None

    if request.method == 'POST' : 
        form = PackageForm(request.POST , instance=package)
        if form.is_valid():
            instance = form.save(commit = False ) 
            instance.created_by = request.user 
            instance.is_created = True 

            available_dates =  request.POST.getlist('available_date')
            instance.available_dates.remove(*instance.available_dates.all())
            print available_dates
            for date in available_dates : 
                d , created = Date.objects.get_or_create(date = date)
                instance.available_dates.add(d)

            instance.save()
            messages.add_message(request , messages.INFO , 'تمت اضافة عرض العمرة بنجاح ')

            return redirect('supplier:agency_profile')

    context['package'] = package
    if package : 
        context['available_dates'] = package.available_dates.values_list('date', flat = True)
    context['calendar'] = get_calendar(3)   
    return render(request , 'supplier/package_crud.html' , context )

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
        return redirect('supplier:agency_profile')

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
