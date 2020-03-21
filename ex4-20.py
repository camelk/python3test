#-*- coding: UTF-8 -*- 
import random

fahr, wind = eval(input("enter three of sides for triangle(ex. Farhrenhiat, wind speed):"))

if -58<= fahr <= 41 and  wind >=2:
	effectiveFahr = 35.74 + 0.6215*fahr - 35.75*(wind**0.16) + 0.4275*fahr*wind**0.16
	print("Effective Temperature: ", format(effectiveFahr,".5f"))
else: # unit == 1 CNY
	print("It is impossible to calculate the effective fahrenheit")
	
	
	
