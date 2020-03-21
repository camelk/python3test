#-*- coding: UTF-8 -*- 
import random

number = eval(input("Enter any integer number: "))



if number % 5 == 0:
	print(number, "is diviced by 5")
if number % 5 == 0 and number % 6 ==0:
	print(number, "is diviced by 5 and 6")
if number % 5 == 0 or number % 6 ==0:
		print(number, "is diviced by 5 or 6")
if number % 6 == 0:
	print(number, "is diviced by 6")
else:
	print(number, "is not diviced by 5 and 6 at the same case")
