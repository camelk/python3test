#-*- coding: UTF-8 -*- 
import random

even = random.randint(0,1)

number = eval(input("enter the number of 1 or 0:"))

if even == number:
	print("Successful...")
else:
	print("Failure....")
