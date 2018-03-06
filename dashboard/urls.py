from django.conf.urls import url , include

from dashboard import views 

urlpatterns	= [ 
	url(r'^dashboard/$' , views.dashboard ,name="dashboard" ) , 
	url(r'^add_agency/$' , views.add_agency ,name="add_agency" ) , 
]