#-*- coding: UTF-8 -*- 

year = eval(input("Enter any year: "))

zodiacYear = year % 12

if zodiacYear == 0:
	print("The Year of the Monkey")
elif zodiacYear == 1:
	print("The Year of the Kichen")
elif zodiacYear == 2:
	print("The Year of the Dog")
elif zodiacYear == 3:
	print("The Year of the Pig")
elif zodiacYear == 4:
	print("The Year of the Rat")
elif zodiacYear == 5:
	print("The Year of the Cow")
elif zodiacYear == 6:
	print("The Year of the Tiger")
elif zodiacYear == 7:
	print("The Year of the Rabiit")
elif zodiacYear == 8:
	print("The Year of the Dragon")
elif zodiacYear == 9:
	print("The Year of the Snake")
elif zodiacYear == 10:
	print("The Year of the Horse")
else:
	print("The Year of the Sheep")												
