from catalogue.models import Package , Agency , MakkahHotel , MadinahHotel 
import random
def run():

	for i in range(5) : 
		MakkahHotel.objects.create(title = 'ahmad' ) 
		MadinahHotel.objects.create(title = 'ahmad' ) 