#-*- coding: UTF-8 -*- 
import random

number1 = random.randint(0,99)
number2 = random.randint(0,99)

answer = eval(input(str(number1) + "*" + str(number2) + "?"))

if number1*number2 == answer:
	print("Successful", "answer:", number1*number2)
else:
	print("You are Wrong","answer:",number1*number2)


