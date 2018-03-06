from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Country(models.Model):
	title = models.CharField(max_length = 50)
	country_code = models.CharField(max_length = 3 , default = 'JO' ) 
	currency = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.title

class Date(models.Model):
	date = models.DateField(auto_now = False , unique = True ) 

class Agency(models.Model):
	created_by = models.ForeignKey(User , null = True )
	supplier_account_agency = models.ForeignKey('Agency', null = True)

	active = models.BooleanField(default = True )
	country = models.ForeignKey(Country , null = True )
	city = models.CharField(max_length = 50 , blank = True ) 
	title = models.CharField(max_length = 50 , blank = True ) 
	about = models.CharField(max_length = 500 , blank = True )

	address = models.CharField(max_length = 50 , blank = True )
	phone_number = models.CharField(max_length = 50 , blank = True )
	email = models.CharField(max_length = 50 , blank = True )
	website = models.CharField(max_length = 50  , blank = True ) 
	facebook_page = models.CharField(max_length = 50 , blank = True )
	logo  = models.FileField(upload_to = 'logos/' , null = True ) 

	available_dates = models.ManyToManyField(Date) 
	# bus_cost = models.IntegerField(default = 0 ) # zero means there are no 
	# flight_cost = models.IntegerField(default = 0 ) # zero means there are no 
	# for suppliers 
	def __unicode__(self):
		return self.title 

class Package(models.Model):
	created_by = models.ForeignKey(User , null = True )
	catalogue_agency = models.ForeignKey(Agency , null = True )
	makkah_hotel = models.ForeignKey('MakkahHotel', null = True )
	madinah_hotel = models.ForeignKey('MadinahHotel', null = True )
	
	single_room_cost = models.IntegerField(default = 0 )
	double_room_cost = models.IntegerField(default = 0 )
	trip_room_cost = models.IntegerField(default = 0 )
	quad_room_cost = models.IntegerField(default = 0 )
	quin_room_cost = models.IntegerField(default = 0 )


	transport = models.CharField(max_length =10 , default ="BUS" ) # choices are('BUS' , 'FLIGHT')


	# agency user section 
	updated_single_room_cost = models.IntegerField(default = 0 )
	updated_double_room_cost = models.IntegerField(default = 0 )
	updated_trip_room_cost = models.IntegerField(default = 0 )
	updated_quad_room_cost = models.IntegerField(default = 0 )
	updated_quin_room_cost = models.IntegerField(default = 0 )

	is_created = models.BooleanField(default = False)
	is_removed = models.BooleanField(default = False)
	is_updated = models.BooleanField(default = False)

	makkah_hotel_title = models.CharField(max_length= 200 , blank = True )
	madinah_hotel_title = models.CharField(max_length= 200 , blank = True )

	# class Meta : 
	# 	unique_together = ('agency' ,'madinah_hotel' , 'makkah_hotel' , 'psport' )

class Hotel(models.Model):
	title = models.CharField(max_length = 50) 
	stars = models.IntegerField(default = 0) 
	photoshots = models.ManyToManyField('Photoshot' , blank = True ) 
	thumbnail = models.FileField(upload_to ='thumbnails/'  , null = True )

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
