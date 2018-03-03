from django import forms 
from customer.models import Reservation

class ReservationForm(forms.ModelForm):
	class Meta : 
		model = Reservation 
		fields = [
		'room_size' , 
		'makkah_hotel' , 
		'madinah_hotel' , 
		'rooms_qty', 
		'guests_qty' , 
		'transport' , 
		'agency' , 
		'customer_address' 
		]
