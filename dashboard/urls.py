from django.conf.urls import url , include

from dashboard import views 

urlpatterns	= [ 
		url(r'^dashboard/$'	,	views.dashboard , name="dashboard" ) ,
		url(r'^dashboard_package/$'	,	views.dashboard_package , name="dashboard_package" ) ,
		url(r'^remove_package/(?P<package_id>\d+)/$'	,	views.remove_package , name="remove_package" ) ,
		url(r'^login_user/$'	,	views.login_user , name="login_user" ) ,
		url(r'^logout_user/$'	,	views.logout_user , name="logout_user" ) ,
		url(r'^register_user/$'	,	views.register_user , name="register_user" ) ,
]