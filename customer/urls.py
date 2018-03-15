from django.conf.urls import url 
from customer import views 

urlpatterns	= [ 
		url(r'^profile/$'	,	views.profile , name="profile" ) , 
		url(r'^cancel_reservation/(?P<reservation_id>\d+)/$' , views.cancel_reservation , name="cancel_reservation" ) , 
		url(r'^change_phone_number/(?P<reservation_id>\d+)/$' , views.change_phone_number , name="change_phone_number" ) , 
		url(r'^reservation/(?P<package_id>\d+)/$'	,	views.reservation , name="reservation" ) , 
	
		url(r'^register_agency/$'	,	views.register_agency , name="register_agency" ) ,
		url(r'^register_customer/$'	,	views.register_customer , name="register_customer" ) ,

		url(r'^login_user/$'	,	views.login_user , name="login_user" ) ,
		url(r'^post_fb_auth/$'	,	views.post_fb_auth , name="post_fb_auth" ) ,
		
		url(r'^logout_user/$'	,	views.logout_user , name="logout_user" ) ,



]