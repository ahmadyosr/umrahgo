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
	user = models.ForeignKey(User , null = True )
	def __unicode__(self):
		return self.title 

class Package(models.Model):
	agency = models.ForeignKey(Agency)
	makkah_hotel = models.ForeignKey('MakkahHotel')
	madinah_hotel = models.ForeignKey('MadinahHotel')
	
	single_room_cost = models.IntegerField(default = 0 )
	double_room_cost = models.IntegerField(default = 0 )
	trip_room_cost = models.IntegerField(default = 0 )
	quad_room_cost = models.IntegerField(default = 0 )
	quin_room_cost = models.IntegerField(default = 0 )

	transport = models.CharField(max_length =10 , default ="BUS") # choices are('BUS' , 'FLIGHT')

	class Meta : 
		unique_together = ('agency' ,'madinah_hotel' , 'makkah_hotel' , 'transport' )

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
