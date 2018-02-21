# class RoomClass(models.Model):
# 	title = models.CharField(max_length = 50 ) 
# 	class_code = models.CharField(max_length = 20 ) 
# 	def __unicode__(self):
# 		return self.title

# class Room(models.Model):
# 	room_class = models.ForeignKey('RoomClass') 
# 	price = models.IntegerField(default = 0 ) 
# 	currency = models.CharField(max_length = 50)

# 	def __unicode__(self):
# 		return self.room_class
import random
from catalogue.models import RoomClass , Room 

room_classes = {
			'DR' : {
				'ar' : '', 
				'en' : 'Double Room' 
			}	, 
			'TR' : {
				'ar' : '', 
				'en' : 'Triple Room' 
			}	, 
			'QR' : {
				'ar' : '', 
				'en' : 'Quadruple Room' 
			}	, 



			'DRMV' : {
				'ar' : '', 
				'en' : 'Double Room Madina View' 
			}	, 
			'TRMV' : {
				'ar' : '', 
				'en' : 'Triple Room Madina View' 
			}	, 
			'QRMV' : {
				'ar' : '', 
				'en' : 'Quadruple Room Madina View' 
			}	, 


			'DRHV' : {
				'ar' : '', 
				'en' : 'Double Room Kaaba View' 
			}	, 
			'TRHV' : {
				'ar' : '', 
				'en' : 'Triple Room Kaaba View' 
			}	, 
			'QRHV' : {
				'ar' : '', 
				'en' : 'Quadruple Room Kaaba View' 
			}	, 


	}
	
def run():
	#populate_room Classes 
	print RoomClass.objects.all()

	# for item in room_classes.items() : 
	# 	print item 
	# 	RoomClass.objects.create(
	# 		title = item[0] , 
	# 		class_code = item[1]['en'] 
	# 	)
	
	# populate rooms 
	for i in range(RoomClass.objects.all().count()): 
		Room.objects.create( 
			room_class = random.choice(RoomClass.objects.all()) , 
			price =random.choice(range(100,400)) , 
			currency = random.choice(['USD' , 'JOD' , 'SAR'] )
		)


	print Room.objects.all()