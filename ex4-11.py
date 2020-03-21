#-*- coding: UTF-8 -*- 
import random

year, month = eval(input("Enter the year and month...(ex, 2000, 2): "))

if month == 1:
	print("Last Date: ", year,"-",month,"-31")
elif  month == 2:
	if year % 4 ==0 and year % 100 !=0 or year % 400==0:
		print("Last Date: ", year,"-",month,"-29")
	else:
		print("Last Date: ", year,"-",month,"-28")
elif month == 3:
	print("Last Date: ", year,"-",month,"-31")
elif month == 4:
	print("Last Date: ", year,"-",month,"-30")
elif month == 5:
	print("Last Date: ", year,"-",month,"-31")
elif month == 6:
	print("Last Date: ", year,"-",month,"-30")
elif month == 7:
	print("Last Date: ", year,"-",month,"-31")
elif month == 8:
	print("Last Date: ", year,"-",month,"-31")
elif month == 9:
	print("Last Date: ", year,"-",month,"-30")
elif month == 10:
	print("Last Date: ", year,"-",month,"-31")		
elif month == 11:
	print("Last Date: ", year,"-",month,"-30")
else:
	print("Last Date: ", year,"-",month,"-31")


