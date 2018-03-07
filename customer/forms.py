from django import forms 
from customer.models import Reservation

class ReservationForm(forms.ModelForm):
	class Meta : 
		model = Reservation 
		fields = [
		'username' , 
		'phone_number' , 
		'departures_qty' , 
		'package', 
		]

