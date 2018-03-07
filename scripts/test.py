from catalogue.models import Package , Agency , MakkahHotel , MadinahHotel 
import random
def run():
	
	packages = Package.objects.all()
	agencies = Agency.objects.all()

	madinah = MadinahHotel.objects.all()
	makkah = MakkahHotel.objects.all()

	for p in packages:
		p.makkah_hotel = random.choice(makkah)
		p.madinah_hotel = random.choice(madinah)
		p.save() 
		