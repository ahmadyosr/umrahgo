from django.conf.urls import url , include

from supplier import views 


urlpatterns	= [ 
	url(r'^agency_profile/$' , views.agency_profile ,name="agency_profile" ) ,
	url(r'^agency/(?P<agency_id>\d+)/$' , views.agency ,name="agency" ) , 
	url(r'^remove_package/(?P<package_id>\d+)/$' , views.remove_package ,name="remove_package" ) , 
	url(r'^update_package/(?P<package_id>\d+)/$' , views.update_package ,name="update_package" ) , 
	url(r'^supplier_package/$' , views.supplier_package ,name="supplier_package" ) ,

]