from django.conf.urls import url , include

from dashboard import views 

urlpatterns	= [ 
	url(r'^dashboard/$' , views.dashboard ,name="dashboard" ) , 
	url(r'^match_agency/$' , views.match_agency ,name="match_agency" ) , 
	url(r'^add_package/(?P<package_id>\d+)/$' , views.add_package ,name="add_package" ) , 
	url(r'^update_package/(?P<package_id>\d+)/$' , views.update_package ,name="update_package" ) , 
	url(r'^remove_package/(?P<package_id>\d+)/$' , views.remove_package ,name="remove_package" ) , 
	url(r'^reject_action/(?P<package_id>\d+)/$' , views.reject_action ,name="reject_action" ) , 
]