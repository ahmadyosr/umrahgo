#-*- encoding:utf-8 -*-
from catalogue.models import Agency , Package  ,Photoshot, Country, MadinahHotel , MakkahHotel  , Room
import random 

def run():

	# popuate packages 


	#-*- encoding:utf-8 -*-
	
	countries = Country.objects.all() 
	titles = [
		'زمزم',
		'طريق النور',
		'عمان',
		'الدلة العالمية',
		'الجمال',
		'البسطامي',
		'نور الهدى',
		'السﻻم',
	]

	madinah_hotels = MadinahHotel.objects.all()
	makkah_hotels = MakkahHotel.objects.all()
	agencies = Agency.objects.all() 
	rooms = Room.objects.all() 
	photos = Photoshot.objects.all()

	# for i in range(len(agencies) * 3)  :
	# 	agency= random.choice(agencies) 
	# 	Package.objects.create(
	# 		agency= agency , 
	# 		title =  agency.title , 
	# 		rooms =random.choice(rooms) , 
	# 		level = random.choice(range(1,5)) , 
	# 		makkah_nights =  random.choice(range(10,15)) , 
	# 		madinah_nights = random.choice(range(3,5))  , 
	# 		thumbnail =  random.choice(photos).file, 
	# 		makkah_hotel = random.choice(makkah_hotels)  , 
	# 		madinah_hotel  =random.choice(madinah_hotels)  , 
	# 	) 

	print Package.objects.all() 
	
	# agency = models.ForeignKey(Agency, null = True 	) 
	# title = models.CharField(max_length = 50) 
	# rooms = models.ForeignKey('Room')
	# level = models.IntegerField(default = 3) 

	# makkah_nights = models.IntegerField(default = 0) 
	# madinah_nights = models.IntegerField(default = 0) 
	# thumbnail = models.FileField(upload_to ='thumbnails/'  , null = True )

	# makkah_hotel = models.ForeignKey('MakkahHotel')
	# madinah_hotel = models.ForeignKey('MadinahHotel')

	# airlines = models.CharField(max_length = 50 , blank = True)
	# ticket_cost = models.IntegerField(default = 0) 
	# 