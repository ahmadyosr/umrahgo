from django import forms 
from catalogue.models import  Agency 


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
		'address' , 
		'website' , 
		'facebook_page' 
		]


class PackageForm(forms.ModelForm):
	class Meta : 
		model = Package
		fields = [
		'makkah_hotel_title' , 
		'madinah_hotel_title' , 
		'makkah_nights' , 
		'madinah_nights' , 
		'double_cost' , 
		'triple_cost' , 
		'quad_cost' , 
		'five_cost' , 
		'transport' , 
		'include_transportation' 
		]


