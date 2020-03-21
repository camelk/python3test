#-*- coding: UTF-8 -*- 
import random


number1 = random.randint(0,100)
number2 = random.randint(0,100)
hab1 = number1 + number2

hab2 = eval(input("enter two integer number for an answer: "))

if hab1 == hab2:
	print("Successful. number1: ",number1, "number2: ", number2, "hab: ", hab1)
else:	
	print("Try...again num1, num2, hab1: ", number1, number2, hab1)
	
	


	
