from django.conf.urls import url , include

from catalogue import views 

urlpatterns	= [ 
		url(r'^$'	,	views.landing_page , name="landing_page" ) , 
		url(r'^about/$'	,	views.about , name="about" ) , 
		url(r'^list/$'	,	views.list , name="list" ) , 
		url(r'^agency/(?P<agency_id>\d+)/$'	,	views.agency , name="agency" ) , 
		url(r'^package/(?P<package_id>\d+)/$'	,	views.package , name="package" ) , 

]