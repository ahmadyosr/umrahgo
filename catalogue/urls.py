from django.conf.urls import url , include

from catalogue import views 

urlpatterns	= [ 
		url(r'^$'	,	views.landing_page , name="landing_page" ) , 
		url(r'^about/$'	,	views.about , name="about" ) , 
		url(r'^contact/$'	,	views.contact , name="contact" ) , 
		url(r'^list/$'	,	views.list , name="list" ) , 
		url(r'^agency/(?P<agency_id>\d+)/$'	,	views.agency , name="agency" ) , 
		url(r'^package/(?P<package_id>\d+)/$'	,	views.package , name="package" ) , 
		url(r'^get_hotel_photos/(?P<hotel_id>\d+)/$'	,	views.get_hotel_photos , name="get_hotel_photos" ) , 
]