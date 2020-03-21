#-*- coding: UTF-8 -*- 
import random


a,b,c,d,e,f = eval(input("enter coefficients for the 2x2 equation(ex:a,b,c,d,e,f):"))

if (a*d-b*c) == 0:
	print("no soultion")
else:	
	x = (e*d - b*f)/(a*d - b*c)
	y = (a*f - e*c)/(a*d - b*c)
	print("x = ", x, "y = ", y)
	
	


	
