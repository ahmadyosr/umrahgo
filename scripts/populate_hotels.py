#-*- encoding:utf-8 -*-
from catalogue.models import MadinahHotel , MakkahHotel  , Photoshot

def run():

	# title = models.CharField(max_length = 50) 
	# stars = models.IntegerField(default = 0) 
	# photoshots = models.ManyToManyField('Photoshot' , blank = True ) 
	# distance_from_center_from_center
	import random
	titles = [ 'فندق دار الإيمان السد ' , 
	'دار الإيمان الخليل' , 
	'لي ميريديان ', 
	'أزكى الصفى' , 
	'ريتاج الريان' , 
	'رمادا دار الفائزين ',
	'موفنبيك ابراج هاجر ',
	'دار التوحيد',
	'رامادا دار الفائزين',
	'حياة ريجينسي',
	]
	madinah_title  = [ 
	'فندق ايلاف طيبة ' , 
	'فندق ديار النخيل' , 
	'مكارم المدينة بلازا' , 
	'ديار الحبيب' , 
	'ديار السﻻم فضي' , 
	'ميراج السﻻم' , 
	]
	photoshots  = Photoshot.objects.all() 
	# for i in range(len(titles)) : 
	# 	hotel = MakkahHotel.objects.create(
	# 		title = random.choice(titles),
	# 		stars = random.choice(range(1,5)) ,
	# 		distance_from_center = random.choice(range(500,1500) ) 
	# 		)	
	# 	hotel.photoshots.add(*photoshots)
	# 	hotel.save() 

	for i in range(len(madinah_title)): 

		hotel = MadinahHotel.objects.create(
			title = random.choice(titles),
			stars = random.choice(range(1,5) ) ,
			distance_from_center = random.choice(range(500,1500) ) 
			)
		hotel.photoshots.add(*photoshots)
		hotel.save() 
