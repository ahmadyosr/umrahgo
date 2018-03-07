from catalogue.models import Agency
from catalogue.models import Country

def agencies(request):

	return {'agencies' : Agency.objects.filter(created_by__is_staff = True).only('id' , 'title') }

def countries(request):
	
	return {'countries' : Country.objects.only('id' , 'title') }
