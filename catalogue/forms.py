from django import forms 
from catalouge.models import Package
class PackageForm(forms.ModelForm):
	class Meta : 
		model = Package
		fields = ['active' , 'hotel' ,'product_class' , 'cost' , 'room_number' ] 

