from django.conf.urls import url , include

from dashboard import views 

urlpatterns	= [ 
		url(r'^dashboard/$'	,	views.dashboard , name="dashboard" ) ,
		url(r'^login_user/$'	,	views.login_user , name="login_user" ) ,
		url(r'^register_user/$'	,	views.register_user , name="register_user" ) ,
]