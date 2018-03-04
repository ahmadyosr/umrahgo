from django.shortcuts import render , redirect 	
from django.http import HttpResponse
from catalogue.models import  Agency , Photoshot , Hotel 
from customer.forms import ReservationForm
# Create your views here.


def landing_page(request):
	# packages = Package.objects.all()[:10]
	packages= [] 
	return render(request ,'index.html' , {'packages': packages} ) 

def agency(request , agency_id ):
	context = {}
	# context['packages'] = Package.objects.filter(agency_id = agency_id ) 
	context['recommended_agencies'] = Agency.objects.all()[:3]
	context['agency'] = Agency.objects.get(id = agency_id)
	return render(request , 'agency.html', context )

def package(request , package_id):
	context = {}
	# context['package'] = Package.objects.get(id = package_id) 
	# context['rooms'] = Room.objects.filter(package = context['package']) 
	# context['packages'] = Package.objects.all()[:3]
	# context['recommended_agencies'] = Agency.objects.all()[:3]

	# context['photos1'] = context['package'].madinah_hotel.photoshots.all() 
	# context['photos2'] = context['package'].makkah_hotel.photoshots.all() 
	
	return render(request , 'detail-page.html' , context )

def list(request):
	country_code = request.GET.get('country_code') 
	# packages = Package.objects.filter(agency__country__country_code = country_code )
	packages = None 
	return render(request , 'result-list.html', {'packages' : packages } )

def about(request):
	return render(request , 'about.html' )


def contact(request):

	return render(request , 'contact.html') 



""" 
Ajax Call from retail_checkout_form.html 
"""
def get_hotel_photos(request, hotel_id ):
	# to calcuulate the total we need :
	# check_in + check_out + meal + rooms_qty

	# calculate total 
	hotel = Hotel.objects.get(id = hotel_id ) 
	photos = hotel.photoshots.all()
	xml = "<RESPONSE>"   

	for photo in photos : 
		xml+= "<PHOTO_URL>"+ str(photo.file.url) + "</PHOTO_URL>"
	xml += "</RESPONSE>"

	return HttpResponse(xml , content_type = "application/xml" )

def get_hotel_rooms_classes(request , hotel_id):
	hotel = Hotel.objects.get(id = hotel_id ) 
	rooms = hotel.rooms.all() 

	xml = "<RESPONSE>"   

	for room in rooms : 
		xml+= "<ROOM>"+ "<ROOM_ID>" +  str(room.id) +"</ROOM_ID>" + "<ROOM_TITLE>" + str(room.title) + "</ROOM_TITLE>" + "</ROOM>"

	xml += "</RESPONSE>"

	return HttpResponse(xml , content_type = "application/xml" )


def get_agency_dates(request , agency_id):
	agency = Agency.objects.get(id = agency_id ) 
	dates = available_dates.rooms.all() 

	xml = "<RESPONSE>"   

	for room in rooms : 
		xml+= "<AGENCY>"+ "<AGENCY_ID>" +  str(room.id) +"</AGENCY_ID>" + "<AGENCY_TITLE>" + str(room.title) + "</AGENCY_TITLE>" + "</AGENCY>"
		
	xml += "</RESPONSE>"

	return HttpResponse(xml , content_type = "application/xml" )



def get_agency_available_dates(request , agency_id):
	agency = Agency.objects.get(id = agency_id ) 
	dates = available_dates.rooms.all() 

	xml = "<RESPONSE>"   

	for date in dates : 
		xml+= "<DATE>"+ str(date.date.isoformat()) +"</DATE>"

	xml += "</RESPONSE>"

	return HttpResponse(xml , content_type = "application/xml" )
