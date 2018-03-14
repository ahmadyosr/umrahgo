from django import forms 
from customer.models import Reservation

class ReservationForm(forms.ModelForm):
	class Meta : 
		model = Reservation
		fields = [
		'package',
		'name',
		'phone_number',
		'departures_qty',
		'departure_date',
		'room_size'
		] 