from django.conf.urls import url , include

from dashboard import views 

urlpatterns	= [ 
	url(r'^dashboard/$' , views.dashboard ,name="dashboard" ) , 
	url(r'^add_agency/$' , views.add_agency ,name="add_agency" ) , 
	url(r'^dashboard_package/$' , views.dashboard_package ,name="dashboard_package" ) ,
	
	url(r'^match_agency/$' , views.match_agency ,name="match_agency" ) , 
	url(r'^approve_add_package/(?P<package_id>\d+)/$' , views.approve_add_package ,name="approve_add_package" ) , 
	url(r'^approve_update_package/(?P<package_id>\d+)/$' , views.approve_update_package ,name="approve_update_package" ) , 
	url(r'^approve_remove_package/(?P<package_id>\d+)/$' , views.approve_remove_package ,name="approve_remove_package" ) , 
	url(r'^reject_action/(?P<package_id>\d+)/$' , views.reject_action ,name="reject_action" ) , 



	url(r'^prices_table/$' , views.prices_table ,name="prices_table" ) , 
]