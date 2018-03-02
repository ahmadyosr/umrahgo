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

class Agency(models.Model):
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

	# for suppliers 
	user = models.ForeignKey(User , null = True )
	def __unicode__(self):
		return self.title 

class Package(models.Model):
	agency = models.ForeignKey(Agency, null = True 	) 
	title = models.CharField(max_length = 50 , blank = True ) 
	level = models.IntegerField(default = 3) 

	makkah_nights = models.IntegerField(default = 0) 
	madinah_nights = models.IntegerField(default = 0) 
	thumbnail = models.FileField(upload_to ='thumbnails/'  , null = True )

	makkah_hotel = models.ForeignKey('MakkahHotel'  , null = True )
	madinah_hotel = models.ForeignKey('MadinahHotel'  , null = True )

	airlines = models.CharField(max_length = 50 , blank = True)
	ticket_cost = models.IntegerField(default = 0) 

	prices_start_from = models.IntegerField(default = 0)
	nights = models.IntegerField(default = 0)

	# upgrades to suite the needs of the registered agencies 
	#rooms 
	
	user = models.ForeignKey(User, null = True)

	makkah_hotel_title = models.CharField(max_length =100, blank = True )
	madinah_hotel_title = models.CharField(max_length =100 , blank = True )

	double_cost = models.IntegerField(default = 0)
	triple_cost = models.IntegerField(default = 0)
	quad_cost = models.IntegerField(default = 0)
	five_cost = models.IntegerField(default = 0)

	transport = models.CharField(max_length = 20 , blank = True  )	
	include_transportation = models.BooleanField(default = False)

	def __unicode__(self):
		return self.title 

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
	class_code = models.CharField(max_length = 20) 
	def __unicode__(self):
		return self.title

class Room(models.Model):
	package = models.ForeignKey(Package , null = True) 
	room_class = models.ForeignKey('RoomClass') 
	currency = models.CharField(max_length = 50)
	person_price = models.IntegerField(default = 0) 
	
	def __unicode__(self):
		return self.room_class.class_code

class Review(models.Model):
	user = models.ForeignKey(User)
	agency = models.ForeignKey('Agency')
	body = models.CharField(max_length = 500) 

	def __unicode__(self):
		return self.user
