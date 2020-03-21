#-*- coding: UTF-8 -*- 
import random

number1, number2, number3 = eval(input("enter the three numbers: "))

if number1 >= number2:
	number1, number2 = number2, number1

if number1 >= number3:
	number1, number3 = number3, number1
	
if number2 >= number3:
	number2, number3 = number3, number2	
	
print(number1, number2, number3)
	
