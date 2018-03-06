from catalogue.models import Package 
from django.contrib.auth.models import User 
from customer.models import UserProfile 

def run():
	
	p = UserProfile.objects.get(id =2) 
	print p 
	# p = UserProfile.objects.last() 
	# print p.id , 'profile.id '
	# print p.user , p.id , 'user name and id ' 
	# u = p.user

	# p.user = None 
	# p.save()
	# u.delete() 
	