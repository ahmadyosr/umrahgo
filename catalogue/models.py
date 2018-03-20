#-*- encoding:UTF-8 -*- 
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.
class Country(models.Model):
	title = models.CharField(max_length = 50)
	country_code = models.CharField(max_length = 3 , default = 'JO' ) 
	currency = models.CharField(max_length = 50)

	def __unicode__(self):
		return unicode(self.title)

class Date(models.Model):
	date = models.DateField(auto_now = False , unique = True ) 
	day = models.CharField(max_length = 50)

class Agency(models.Model):
	created_by = models.ForeignKey(User , null = True )
	supplier_account_agency = models.ForeignKey('Agency', null = True , blank = True )

	active = models.BooleanField(default = True )
	city = models.ForeignKey(Country , null = True )
	title = models.CharField(max_length = 50 , blank = True ) 
	about = models.CharField(max_length = 500 , blank = True )

	address = models.CharField(max_length = 50 , blank = True )
	phone_number = models.CharField(max_length = 50 , blank = True )
	email = models.CharField(max_length = 50 , blank = True )
	website = models.CharField(max_length = 50  , blank = True ) 
	facebook_page = models.CharField(max_length = 50 , blank = True )
	logo  = models.FileField(upload_to = 'logos/' , null = True ) 

	prices_start_from = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return self.title 

class Package(models.Model):
	# duration
	nights = models.IntegerField(null = True , blank = True)
	days = models.IntegerField(null = True , blank = True)
	makkah_nights = models.IntegerField(null = True , blank = True)
	madinah_nights = models.IntegerField(null = True , blank = True)
	meal = models.CharField(max_length= 100, blank = True)
	# management 
	title = models.CharField(max_length =200 , blank = True) 
	created_by = models.ForeignKey(User , null = True )
	catalogue_agency = models.ForeignKey(Agency , null = True )
	available_dates = models.ManyToManyField(Date, blank = True ) #in scope of three months

	# accomodation
	makkah_hotel = models.ForeignKey('MakkahHotel', null = True )
	madinah_hotel = models.ForeignKey('MadinahHotel', null = True )
	
	makkah_hotel_title = models.CharField(max_length= 200 , blank = True )
	makkah_hotel_stars = models.CharField(max_length= 200 , blank = True )
	makkah_hotel_distance = models.IntegerField(default = 0 ) #>>new
	
	madinah_hotel_title = models.CharField(max_length= 200 , blank = True )
	madinah_hotel_stars = models.CharField(max_length= 200 , blank = True )
	madinah_hotel_distance = models.IntegerField(default = 0 ) #>>new

	# transport
	bus_model = models.CharField(max_length=100 , blank = True) #>>new
	bus_capacity = models.IntegerField(null = True,blank = True) #>>new

	airlines = models.CharField(max_length =100 , blank = True) # choices are('BUS' , 'FLIGHT')
	transport = models.CharField(max_length =10 , default ="BUS" ) # choices are('BUS' , 'FLIGHT')

	#prices 
	single_room_cost = models.IntegerField(default = 0 )
	double_room_cost = models.IntegerField(default = 0 )
	trip_room_cost = models.IntegerField(default = 0 )
	quad_room_cost = models.IntegerField(default = 0 )
	quin_room_cost = models.IntegerField(default = 0 )

	updated_single_room_cost = models.IntegerField(default = 0 )
	updated_double_room_cost = models.IntegerField(default = 0 )
	updated_trip_room_cost = models.IntegerField(default = 0 )
	updated_quad_room_cost = models.IntegerField(default = 0 )
	updated_quin_room_cost = models.IntegerField(default = 0 )
	
	prices_start_from = models.IntegerField(default = 0)
	
	# agency's user action
	is_created = models.BooleanField(default = False)
	is_removed = models.BooleanField(default = False)
	is_updated = models.BooleanField(default = False)
	

 	@property
	def catalogue_title(self):
		# return 'fdsfds' 
		if self.transport == "BUS" : 
			travel = "السفر براً"
		else: 
			travel = "السفر جواً"

		try : 
			stars = self.makkah_hotel.stars
		except AttributeError : 
			stars = '0'
		if self.nights > 0 :
			nights_phrase = ' ' +str(self.nights)+' ليالي'
		else : 
			nights_phrase = ' '

		return unicode("فندق ") +unicode(self.makkah_hotel.title) \
		+ " "+ unicode(stars)\
		+ unicode(" نجوم ")+ unicode(travel) + nights_phrase

	def __unicode__(self):
		if self.makkah_hotel and self.madinah_hotel : 
			return self.catalogue_title
		else : 
			return str(self.id)

class Hotel(models.Model):
	title = models.CharField(max_length = 50) 
	stars = models.IntegerField(default = 0) 
	photoshots = models.ManyToManyField('Photoshot' , blank = True ) 
	thumbnail = models.FileField(upload_to ='thumbnails/'  , null = True , blank = True  )
	distinct = models.CharField(max_length =200 , blank = True )
	def __unicode__(self):
		return self.title

class MakkahHotel(Hotel):
	distance_from_center  = models.IntegerField(default = 0) 
	
	def __unicode__(self):
		return self.title

class MadinahHotel(Hotel):
	distance_from_center  = models.IntegerField(default = 0) 
	def __unicode__(self):
		return self.title

class Photoshot(models.Model):
	file = models.FileField(upload_to = "photoshots")

class RoomClass(models.Model):
	title = models.CharField(max_length = 50 ) 
	class_code = models.CharField(max_length = 20 , unique = True ) 
	def __unicode__(self):
		return self.title




## signals for orders postsave 
@receiver(post_save , sender= Package) 
def post_save_package(sender ,created, instance,**kwargs ):
	# calculate the start_from_prices for catalogue_agency 
	if instance.catalogue_agency : 
		agency = instance.catalogue_agency
		agency_start_from = agency.prices_start_from
		package_start_from = instance.prices_start_from


		single = instance.single_room_cost
		double = instance.double_room_cost
		trip = instance.trip_room_cost
		quad = instance.quad_room_cost
		quin = instance.quin_room_cost
		prices = (single , double ,trip , quad , quin )

		for p in prices : 
			if p > 0 : 
				if agency_start_from == 0 : 
					agency_start_from = p 
				if p < agency_start_from : 
					agency_start_from = p

				if package_start_from == 0 : 
					package_start_from = p 
				if p < package_start_from : 
					package_start_from = p 

		agency.prices_start_from = agency_start_from 
		agency.save()

		Package.objects.filter(id= instance.id).update(prices_start_from = package_start_from)

	return 