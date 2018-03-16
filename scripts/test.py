import datetime 
def run():
	start = datetime.date.today().replace(day=1)
	one_day_delta = datetime.timedelta(days = 1) 
	dates = [] 
	start_month = start.month
	i = 0 ;
	while i < 3:
		dates += [start] 
		start = start + one_day_delta

		print start_month , ' !=?' , start.month 
		print start
		if start_month != start.month :
			start_month = start.month
			i = i + 1

