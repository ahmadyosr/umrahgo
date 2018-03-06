from django.shortcuts import render , redirect
from django.http import HttpResponse
from catalogue.models import Agency
from supplier.forms import AgencyForm

# Create your views here.
def dashboard(request):
	if not request.user.is_staff  : 
		return HttpResponse(status = 404 )

	context = {}
	context['agencies'] = Agency.objects.filter(created_by__is_staff = True)
	return render(request , 'dashboard/dashboard.html' , context )

def add_agency(request):
	if request.method == 'POST' and request.user.is_staff: 
		form = AgencyForm(request.POST)
		if form.is_valid():
			instance = form.save(commit = False )
			instance.created_by = request.user
			instance.save() 
			return redirect('dashboard')
	return render(request , 'dashboard/add_agency.html')