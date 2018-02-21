from django.shortcuts import render
from django.http import HttpResponse
from catalogue.models import Package  , Room 
# Create your views here.


def landing_page(request):
	packages = Package.objects.all()[:10]
	return render(request ,'index.html' , {'packages': packages} ) 

def agency(request , agency_id ):
	return render(request , 'result-grid.html' )

def package(request , package_id):
	context = {}
	context['package'] = Package.objects.get(id = package_id) 
	context['rooms'] = Room.objects.filter(package = context['package']) 

	return render(request , 'detail-page.html' , context )

def list(request):
	packages = Package.objects.all()
	return render(request , 'result-list.html', {'packages' : packages } ) 

def about(request):
	return render(request , 'about.html' )

