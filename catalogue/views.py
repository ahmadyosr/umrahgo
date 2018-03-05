from django.shortcuts import render , redirect 	
from django.http import HttpResponse
from catalogue.models import  Agency , Photoshot , Hotel , Package
from customer.forms import ReservationForm
# Create your views here.


def landing_page(request):
	packages= [] 
	return render(request ,'index.html' , {'packages': packages} ) 

def agencies_list(request):

	return render(request , 'agencies_list.html', {'range_list': range(10)}  )

def agency(request , agency_id ):
	context = {}
	context['recommended_agencies'] = Agency.objects.all()[:3]
	context['agency'] = Agency.objects.get(id = agency_id)
	return render(request , 'agency.html', context )

def package(request , package_id):
	context = {}

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


"""
when change agency change the following
1- hotels
1.5- hotel rooms
2- available dates 
3- transport method 
"""

def get_agency_makkah_hotels(request, agency_id) : 
	hotels = []
	makkah_hotels = Package.objects.filter(id = agency_id).values('makkah_hotel__id', 'makkah_hotel__title')
	for hotel in makkah_hotels : 
		if hotel not in hotels:
			hotels.append(hotel)

	xml = "<RESPONSE>"   

	for hotel in hotels : 
		xml += "<HOTEL><HOTEL_ID>"+ str(hotel.id) +"</HOTEL_ID>" \
		+ "<HOTEL_TITLE>"+ str(hotel.title) +"</HOTEL_TITLE></HOTEL>"

	xml += "</RESPONSE>"

	return HttpResponse(xml , content_type = "application/xml" )

# on change of makkah hotel choices
def get_madinah_hotels(request, agency_id ,  makkah_hotel_id ) : 
	madinah_hotels = Package.objects.filter(
		agency__id = agency_id ,
		makkah_hotel__id = makkah_hotel_id
		).values(
		'madinah_hotel__id' ,
		'madinah_hotel__title', 
		)

	xml = "<RESPONSE>"   

	for hotel in madinah_hotels : 
		xml += "<HOTEL><HOTEL_ID>"+ str(hotel.id) +"</HOTEL_ID>" \
		+ "<HOTEL_TITLE>"+ str(hotel.title) +"</HOTEL_TITLE></HOTEL>"

	xml += "</RESPONSE>"

	return HttpResponse(xml , content_type = "application/xml" )

	return 

# on change of madinah hotel 
def get_package_rooms(request , agency_id , makkah_hotel_id , madinah_hotel_id, transport ):
	# uniqueness of this query is guaranteed in schema design 
	package = Package.objects.get(makkha_hotel__id = makkah_hotel_id , madinah_hotel__id = madinah_hotel_id , transport = transport ) 
	xml = "<RESPONSE>"   

	if package.single_room_cost > 0 : 
		xml += "<SINGLE_COST>"+ str(package.single_room_cost) +"</SINGLE_COST>"
		
	if package.double_room_cost > 0 : 
		xml += "<DOUBLE_COST>"+ str(package.double_room_cost) +"</DOUBLE_COST>"

	if package.trip_cost > 0 : 
		xml += "<TRIP_COST>"+ str(package.trip_cost) +"</TRIP_COST>"

	if package.quad_cost > 0 : 
		xml += "<QUAD_COST>"+ str(package.quad_cost) +"</QUAD_COST>"

	if package.quin_cost > 0 : 
		xml += "<QUIN_COST>"+ str(package.quin_cost) +"</QUIN_COST>"

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

def get_package_travel_methods(request , madinah_hotel_id , makkah_hotel_id ):
	package = Package.objects.filter(makkha_hotel__id = makkah_hotel_id , madinah_hotel__id = madinah_hotel_id )

	xml = "<RESPONSE>"   

	for date in dates : 
		xml+= "<DATE>"+ str(date.date.isoformat()) +"</DATE>"

	xml += "</RESPONSE>"


	return HttpResponse(xml , content_type = "application/xml" )
