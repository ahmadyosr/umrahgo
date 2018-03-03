from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 
from django.dispatch import receiver
from catalogue.models import RoomClass , MakkahHotel , MadinahHotel , Agency 
# Create your models here.

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone_number = models.CharField(max_length = 15 , blank = True)

class Reservation(models.Model):
	user = models.ForeignKey(User)

	room_size = models.ForeignKey(RoomClass)
	makkah_hotel = models.ForeignKey(MakkahHotel)
	madinah_hotel = models.ForeignKey(MadinahHotel)
	rooms_qty = models.IntegerField(default = 0 )
	guests_qty = models.IntegerField(default = 0 ) 
	transport = models.CharField(max_length = 50 )
	agency = models.ForeignKey(Agency)
	departure_date = models.DateField(auto_now = False) 
	customer_address = models.CharField(max_length= 200 )

@receiver(post_save , sender= User) 
def post_save_order(sender ,created, instance,**kwargs ):
	if created : 
		UserProfile.objects.create(user = instance)
