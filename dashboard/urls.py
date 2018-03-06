from django.conf.urls import url , include

from dashboard import views 

urlpatterns	= [ 
	url(r'^dashboard/$' , views.dashboard ,name="dashboard" ) , 
]