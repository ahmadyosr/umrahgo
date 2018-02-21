from django.contrib import admin
from catalogue.models import ( 
	Package , 
	Hotel , 
	MakkahHotel , 
	MadinahHotel , 
	Photoshot , 
	Country , 
	Agency, 
	RoomClass , 
	Room , 
	Review 
	)
# Register your models here.
admin.site.register(Package)
admin.site.register(Hotel)
admin.site.register(MakkahHotel) 
admin.site.register(MadinahHotel) 
admin.site.register(Photoshot) 
admin.site.register(Country) 
admin.site.register(Agency) 
admin.site.register(RoomClass) 
admin.site.register(Room) 
admin.site.register(Review)