from django.contrib import admin
from catalogue.models import ( 
	Hotel , 
	MakkahHotel , 
	MadinahHotel , 
	Photoshot , 
	Country , 
	Agency, 
	RoomClass, 
	Package
	)
# Register your models here.
admin.site.register(Hotel)
admin.site.register(MakkahHotel) 
admin.site.register(MadinahHotel) 
admin.site.register(Photoshot) 
admin.site.register(Country) 
admin.site.register(Agency) 
admin.site.register(RoomClass) 
admin.site.register(Package) 
