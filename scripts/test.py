from catalogue.models import Package , Agency , MakkahHotel , MadinahHotel 
import random
def run():
	
	package = Package.objects.exclude(catalogue_agency = None).first()
	print package.id , 'id'
	print package.prices_start_from 
	# package.single_room_cost = 2
	# package.save()
	print package.prices_start_from

