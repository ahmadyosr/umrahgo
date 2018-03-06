from django.conf.urls import url , include

from dashboard import views 

urlpatterns	= [ 
	url(r'^dashboard/$' , views.dashboard ,name="dashboard" ) , 
	url(r'^dashboard_package/$' , views.dashboard_package ,name="dashboard_package" )
]