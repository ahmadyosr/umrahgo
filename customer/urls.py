from django.conf.urls import url 
from customer import views 

urlpatterns	= [ 
		url(r'^profile/$'	,	views.profile , name="profile" ) , 
		url(r'^reservation/$'	,	views.reservation , name="reservation" ) , 
		url(r'^login_user/$'	,	views.login_user , name="login_user" ) ,
		url(r'^logout_user/$'	,	views.logout_user , name="logout_user" ) ,
		url(r'^register_user/$'	,	views.register_user , name="register_user" ) ,
]