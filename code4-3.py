#-*- coding: UTF-8 -*- 

day = 0

question1 = "Set1?\n"+ \
	"1 3 5 7\n" + \
	"9 11 13 15\n" + \
	"17 19 21 23\n" + \
	"25 27 29 31\n" + \
	"\nEnter the either 0(NO) or 1(YES): "
	
answer = eval(input(question1))

if answer == 1:
	day += 1
	
# enter answer for the second question from a user
question2 = "Set2?\n"+ \
	"2 3 6 7\n" + \
	"10 11 14 15\n" + \
	"18 19 22 23\n" + \
	"26 27 30 31\n" + \
	"\nEnter the either 0(NO) or 1(YES): "
 
answer = eval(input(question2))

if answer == 1:
	day += 2


# enter answer for the third question from a user
question3 = "Set3?\n"+ \
	"4 5 6 7\n" + \
	"12 13 14 15\n" + \
	"20 21 22 23\n" + \
	"28 29 30 31\n" + \
	"\nEnter the either 0(NO) or 1(YES): "
 
answer = eval(input(question3))

if answer == 1:
	day += 4
	
		
# enter answer for the forth question from a user
question4 = "Set4?\n"+ \
	"8 9 10 11\n" + \
	"12 13 14 15\n" + \
	"24 25 26 27\n" + \
	"28 29 30 31\n" + \
	"\nEnter the either 0(NO) or 1(YES): "
 
answer = eval(input(question4))

if answer == 1:
	day += 8
	
# enter answer for the fifth question from a user
question5 = "Set5?\n"+ \
	"16 17 18 19\n" + \
	"20 21 22 23\n" + \
	"24 25 26 27\n" + \
	"28 29 30 31\n" + \
	"\nEnter the either 0(NO) or 1(YES): "
 
answer = eval(input(question5))

if answer == 1:
	day += 16	
	
print("\n your birthday?: " + "is " + str(day) +" day.")
