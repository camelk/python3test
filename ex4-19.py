#-*- coding: UTF-8 -*- 
import random

a, b, c = eval(input("enter three of sides for triangle(ex.a,b,c):"))

if a+b >= c and a+c >= b and c+b >= a:
	print("It is possible to draw the triange with the sides")
	length = a + b + c
	print("the length of three sides of triangle:", length)	
else: # unit == 1 CNY
	print("It is impossible to draw the triange with the side")
	
