from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from catalogue.models import Photoshot , MakkahHotel , MadinahHotel , Agency
@login_required
def profile(request):
	# default session varibales 
	# [(u'_auth_user_hash', u'ed93fd3a13d66bb6d7fcee07ec35abfc5ec7d21d'), 
	# (u'_auth_user_id', u'14'), 
	# (u'_auth_user_backend', u'django.contrib.auth.backends.ModelBackend')]
	if request.session.get('pending_reservation'):
		print 'fdsfdas'	

	return render(request , 'profile.html'  )

def reservation(request):
	context = {}
	next_ = False 

	if request.GET.get('next_'):
		for item in request.GET.items():
			request.session[item[0]] = item[1]
		return redirect('register_user')
	
	context['next_'] = next_
	context['photos'] = Photoshot.objects.all()[:6]
	context['makkah_hotels'] = MakkahHotel.objects.only('id' ,'title' ,'stars') 
	context['agencies'] = Agency.objects.filter(active = True )
	return render(request , 'reservation.html' , context )

