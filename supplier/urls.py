from django.conf.urls import url , include

from supplier import views 

urlpatterns	= [ 
	url(r'^supplier/$' , views.supplier ,name="supplier" ) , 
	url(r'^supplier_package/$' , views.supplier_package ,name="supplier_package" )
]