#-*- encoding:utf-8 -*-
from catalogue.models import Agency , Package  ,Photoshot, Country
import random 
def run():
	# populate agencies 

	# country = models.ForeignKey(Country) 
	# city = models.CharField(max_length = 50) 
	# title = models.CharField(max_length = 50) 
	# about = models.CharField(max_length = 500)
	

	# address = models.CharField(max_length = 50)
	# phone_number = models.CharField(max_length = 50)
	# email = models.CharField(max_length = 50)
	# facebook_page = models.CharField(max_length = 50)
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
	for i in range(len(titles) * 2)  :

		Agency.objects.create(
			country = random.choice(countries), 
			city = random.choice(['عمان' , 'الزرقاء']) , 
			title  = random.choice(titles) , 
			about = 'وكالة سفر في الأردن' , 
			address = 'شارع مكة أو شارع المدينة', 
			phone_number = random.choice(range(1299999, 9299999)) , 
			email = 'agency@example.com' , 
			facebook_page  = 'www.facebook.com' 
		) 
