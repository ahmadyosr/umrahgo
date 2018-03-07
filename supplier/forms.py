from django import forms 
from catalogue.models import  Agency , Package

class AgencyForm(forms.ModelForm):
	phone_number= forms.CharField(required = False ) 
	email= forms.CharField(required = False ) 
	address = forms.CharField(required = False ) 
	address = forms.CharField(required = False ) 
	website = forms.CharField(required = False ) 
	facebook_page= forms.CharField(required = False ) 
	class Meta : 
		model = Agency 
		fields = [
		'country' , 
		'city' , 
		'title' , 
		'phone_number', 
		'email' , 
		'address' , 
		'website' , 
		'facebook_page' 
		]


class PackageForm(forms.ModelForm):
	class Meta : 
		model = Package
		fields = [
		'makkah_hotel' , 
		'madinah_hotel' , 
		'makkah_hotel_title' , 
		'madinah_hotel_title' ,
		'updated_single_room_cost' , 
		'updated_double_room_cost', 
		'updated_trip_room_cost', 
		'updated_quad_room_cost', 
		'updated_quin_room_cost', 
		'transport' , 
		]


class UpdatePackageForm(forms.ModelForm):
	class Meta : 
		model = Package
		fields = [
		'updated_single_room_cost' , 
		'updated_double_room_cost', 
		'updated_trip_room_cost', 
		'updated_quad_room_cost', 
		'updated_quin_room_cost', 
		]


