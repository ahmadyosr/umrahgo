from django.shortcuts import render

# Create your views here.
def dashboard(requset):

	return render(request , 'dashboard/dashboard.html')