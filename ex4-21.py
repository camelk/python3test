#-*- coding: UTF-8 -*- 
import random

year = eval(input("enter a year:"))
month = eval(input("enter a month:"))
day = eval(input("enter a day:"))

print("it is ", year,"-",month,"-",day)
if month == 1:
	month = 13
if month == 2:
	month = 14
	
#if year % 100 == 0:
#	century = year%100-1;
#else:
#	century = year // 100 + 1

#print("year:", year," is ", century, "Cenury")
q = day
m = month
k = year % 100
j = year // 100

h = (q + (26*(m+1))//10 + k + k // 4 + j//100 + 2 * j) % 7

if h == 0: # saturday
	print("It is Saturday, today")
elif h == 1: # sunday
	print("It is Sundday, today")
elif h == 2: # monday
	print("It is Monday, today")
elif h == 3: # tueday
	print("It is Tuesday, today")
elif h == 4: # wednesday
	print("It is Wednesday, today")
elif h == 5: # thursday
	print("It is Thursday, today")
elif h == 6: # frinday	
	print("It is Friday, today")
else:
	print("We have no idea what day it is today")
	
	
