#-*- coding: UTF-8 -*- 
import random



today = eval(input("what day is it, today(0-6, sun-sat):"))
day = eval(input("elapsed day to the future: "))

future = (today+day) % 7

if today % 7 == 0:
	print("Today is Sunday.", end=" ")
	if future % 7 == 0:
		print("The Future Day is Sunday.","Future NO:", future)
	elif future % 7 == 1:
		print("The Future Day is Monday.","Future NO:", future)
	elif future % 7 == 2:
		print("The Future Day is Tuesday.","Future NO:", future)
	elif future % 7 == 3:
		print("The Future Day  is Wednesday.","Future NO:", future)
	elif future % 7 == 4:
		print("The Future Day is Thursday.","Future NO:", future)
	elif future % 7 == 5:
		print("The Future Day is Fridday.","Future NO:", future)
	else: #today % 7 = 6
		print("The Future Day  is Saturday.","Future NO:", future)
		
elif today % 7 == 1:
	print("Today is Monday.", end=" ")
	if future % 7 == 0:
		print("The Future Day is Sunday.","Future NO:", future)
	elif future % 7 == 1:
		print("The Future Day is Monday.","Future NO:", future)
	elif future % 7 == 2:
		print("The Future Day is Tuesday.","Future NO:", future)
	elif future % 7 == 3:
		print("The Future Day  is Wednesday.","Future NO:", future)
	elif future % 7 == 4:
		print("The Future Day is Thursday.","Future NO:", future)
	elif future % 7 == 5:
		print("The Future Day is Fridday.","Future NO:", future)
	else: #today % 7 = 6
		print("The Future Day  is Saturday.","Future NO:", future)
	
	
elif today % 7 == 2:
	print("Today is Tuesday.", end=" ")
	if future % 7 == 0:
		print("The Future Day is Sunday.","Future NO:", future)
	elif future % 7 == 1:
		print("The Future Day is Monday.","Future NO:", future)
	elif future % 7 == 2:
		print("The Future Day is Tuesday.","Future NO:", future)
	elif future % 7 == 3:
		print("The Future Day  is Wednesday.","Future NO:", future)
	elif future % 7 == 4:
		print("The Future Day is Thursday.","Future NO:", future)
	elif future % 7 == 5:
		print("The Future Day is Fridday.","Future NO:", future)
	else: #today % 7 = 6
		print("The Future Day  is Saturday.","Future NO:", future)
		
elif today % 7 == 3:
	print("Today is Wednesday.", end=" ")
	if future % 7 == 0:
		print("The Future Day is Sunday.","Future NO:", future)
	elif future % 7 == 1:
		print("The Future Day is Monday.","Future NO:", future)
	elif future % 7 == 2:
		print("The Future Day is Tuesday.","Future NO:", future)
	elif future % 7 == 3:
		print("The Future Day  is Wednesday.","Future NO:", future)
	elif future % 7 == 4:
		print("The Future Day is Thursday.","Future NO:", future)
	elif future % 7 == 5:
		print("The Future Day is Fridday.","Future NO:", future)
	else: #today % 7 = 6
		print("The Future Day  is Saturday.","Future NO:", future)
	
elif today % 7 == 4:
	print("Today is Thursday.", end=" ")
	if future % 7 == 0:
		print("The Future Day is Sunday.","Future NO:", future)
	elif future % 7 == 1:
		print("The Future Day is Monday.","Future NO:", future)
	elif future % 7 == 2:
		print("The Future Day is Tuesday.","Future NO:", future)
	elif future % 7 == 3:
		print("The Future Day  is Wednesday.","Future NO:", future)
	elif future % 7 == 4:
		print("The Future Day is Thursday.","Future NO:", future)
	elif future % 7 == 5:
		print("The Future Day is Fridday.","Future NO:", future)
	else: #today % 7 = 6
		print("The Future Day  is Saturday.","Future NO:", future)
	
elif today % 7 == 5:
	print("Today is Fridday.", end =" ")
	if future % 7 == 0:
		print("The Future Day is Sunday.","Future NO:", future)
	elif future % 7 == 1:
		print("The Future Day is Monday.","Future NO:", future)
	elif future % 7 == 2:
		print("The Future Day is Tuesday.","Future NO:", future)
	elif future % 7 == 3:
		print("The Future Day  is Wednesday.","Future NO:", future)
	elif future % 7 == 4:
		print("The Future Day is Thursday.","Future NO:", future)
	elif future % 7 == 5:
		print("The Future Day is Fridday.","Future NO:", future)
	else: #today % 7 = 6
		print("The Future Day  is Saturday.","Future NO:", future)
		
else: #today % 7 = 6
	print("Today is Saturday.", end = " ")
	if future % 7 == 0:
		print("The Future Day is Sunday.","Future NO:", future)
	elif future % 7 == 1:
		print("The Future Day is Monday.","Future NO:", future)
	elif future % 7 == 2:
		print("The Future Day is Tuesday.","Future NO:", future)
	elif future % 7 == 3:
		print("The Future Day  is Wednesday.","Future NO:", future)
	elif future % 7 == 4:
		print("The Future Day is Thursday.","Future NO:", future)
	elif future % 7 == 5:
		print("The Future Day is Fridday.","Future NO:", future)
	else: #today % 7 = 6
		print("The Future Day  is Saturday.","Future NO:", future)

			

	
	


	
