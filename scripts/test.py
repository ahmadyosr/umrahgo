from catalogue.models import Package 
from django.contrib.auth.models import User 

def run():
	
	user = User.objects.get()
	package = Package.objects.get()	

	print user.id , 'user id ' 
	print package.id , 'package id '
	# package.user = user 
	# package.save()
	# user.delete() 