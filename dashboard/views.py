from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from catalogue.models import Agency , Package
from supplier.forms import AgencyForm
from django.db.models import Q 
# Create your views here.
def dashboard(request):
	if not request.user.is_staff  : 
		return HttpResponse(status = 404 )

	context = {}
	context['agencies'] = Agency.objects.filter(created_by__is_staff = True)
	context['packages'] = Package.objects.filter(Q(is_created = True ) | Q(is_removed = True) | Q(is_updated = True ) ) 
	return render(request , 'dashboard/dashboard.html' , context )

def add_agency(request):
	
	return render(request,'dashboard/add_agency.html')

def match_agency(request):
	if request.method == 'POST' : 
		agency_id = request.POST.get('agency')
		matched_id =request.POST.get('matched_agency')

		Agency.objects.filter(id = agency_id).update(supplier_account_agency = matched_id)


		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	return HttpResponse(status = 404 )

def add_package(request , package_id ):
	package = Package.objects.get(id = package_id) 
	supplier_agency = 
	package.catalogue_agency = supplier_agency
	package.save()
	return HttpResponse("succesfuly done ")
def update_package(request , package_id ):
	return 

def remove_package(request , package_id ):
	return 

def reject_action(request , package_id ):
	return 
