#-*- encoding:UTF-* -*-
from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from catalogue.models import Agency , Package
from supplier.forms import AgencyForm
from django.db.models import Q 
from django.contrib import messages 
from django.db.models import ObjectDoesNotExist


# utility functions 
def migrate_prices(package):
	package.single_room_cost = package.updated_single_room_cost
	package.double_room_cost = package.updated_double_room_cost
	package.trip_room_cost = package.updated_trip_room_cost
	package.quad_room_cost = package.updated_quad_room_cost
	package.quin_room_cost = package.updated_quin_room_cost
	return

# Create your views here.
def dashboard(request):
	if not request.user.is_staff  : 
		return HttpResponse(status = 404 )

	context = {}
	context['agencies'] = Agency.objects.filter(created_by__is_staff = True)
	context['packages'] = Package.objects.exclude(created_by__is_staff = True).filter(Q(is_created = True ) | Q(is_removed = True) | Q(is_updated = True ) ) 
	context['suppliers_agencies'] = Agency.objects.filter(created_by__is_staff = False).order_by('-id') 

	return render(request , 'dashboard/dashboard.html' , context )

def add_agency(request):
	if request.method == 'POST' : 
		form = AgencyForm(request.POST)
		if form.is_valid() : 
			instance = form.save(commit = False) 
			instance.created_by = request.user 
			instance.save() 
			return redirect('dashboard:dashboard')
		else : 
			print form.errors 

	return render(request,'dashboard/add_agency.html')

def match_agency(request):
	if request.method == 'POST' : 
		agency_id = request.POST.get('agency')
		matched_id =request.POST.get('matched_agency')
		
		Agency.objects.filter(id = agency_id).update(supplier_account_agency = matched_id)

		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	return HttpResponse(status = 404 )


def approve_add_package(request , package_id ):
	# add package means to assign a catalogue_agency for the package 
	package = Package.objects.get(id = package_id) 

	supplier_user = package.created_by
	supplier_agency = Agency.objects.get(created_by = supplier_user)
	try : 
		catalogue_agency = Agency.objects.get(supplier_account_agency = supplier_agency)
	except ObjectDoesNotExist : 
		messages.add_message(request , messages.INFO , 'package agency not matched to agency')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	package.catalogue_agency = catalogue_agency
	package.is_created = False
	migrate_prices(package)
	package.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def approve_update_package(request , package_id ):
	package = Package.objects.get(id = package_id)
	migrate_prices(package)
	package.is_updated = False
	package.save() 

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def approve_remove_package(request , package_id ):
	Package.objects.get(id = package_id).delete() 

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def reject_action(request , package_id ):
	package = Package.objects.get(id = package_id) 

	if package.is_updated : 
		package.single_room_cost = package.updated_single_room_cost
		package.double_room_cost = package.updated_double_room_cost
		package.trip_room_cost = package.updated_trip_room_cost
		package.quad_room_cost = package.updated_quad_room_cost
		package.quin_room_cost = package.updated_quin_room_cost


	package.is_updated = False
	package.is_removed = False  
	package.save() 
	if package.is_created : 
		package.delete() 

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def dashboard_package(request):
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
    return render(request , 'dashboard/package_crud.html' , context )
