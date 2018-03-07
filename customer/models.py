from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 
from django.dispatch import receiver
from catalogue.models import RoomClass , MakkahHotel , MadinahHotel , Agency 
# Create your models here.

# Create your models here.

class Reservation(models.Model):
	username = models.CharField(max_length =100) 
	phone_number = models.CharField(max_length = 200)

	departures_qty = models.IntegerField(default = 1)
	package = models.IntegerField(null = True)
