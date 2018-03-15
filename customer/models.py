from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 
from django.dispatch import receiver
from catalogue.models import Package , Date
# Create your models here.

class Reservation(models.Model):

	user = models.ForeignKey(User, null = True)
	package = models.ForeignKey(Package, null = True)
	name = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 100)
	departures_qty = models.CharField(max_length = 100)
	departure_date = models.DateField(auto_now = False)
	room_size = models.CharField(max_length = 100)
	departure_cost = models.IntegerField(default = 0)
	
	is_paid = models.BooleanField(default = False )
	is_canceled = models.BooleanField(default = False)
