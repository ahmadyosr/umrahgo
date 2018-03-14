from django.conf.urls import url 
from customer import views 

urlpatterns	= [ 
		url(r'^profile/$'	,	views.profile , name="profile" ) , 
		url(r'^cancel_reservation/(?P<reservation_id>\d+)/$' , views.cancel_reservation , name="cancel_reservation" ) , 
		url(r'^change_phone_number/(?P<reservation_id>\d+)/$' , views.change_phone_number , name="change_phone_number" ) , 
		url(r'^reservation/(?P<package_id>\d+)/$'	,	views.reservation , name="reservation" ) , 
		url(r'^login_agency/$'	,	views.login_agency , name="login_agency" ) ,
		url(r'^login_customer/$'	,	views.login_customer , name="login_customer" ) ,

		url(r'^logout_user/$'	,	views.logout_user , name="logout_user" ) ,
		url(r'^register_agency/$'	,	views.register_agency , name="register_agency" ) ,
		url(r'^register_customer/$'	,	views.register_customer , name="register_customer" ) ,



]