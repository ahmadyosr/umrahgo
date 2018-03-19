from django import forms 
from customer.models import Reservation

class ReservationForm(forms.ModelForm):
	departure_cost = forms.IntegerField(required = False)
	class Meta : 
		model = Reservation
		fields = [
		'package',
		'name',
		'phone_number',
		'departures_qty',
		# 'departure_date',
		'room_size',
		'departure_cost'
		] 