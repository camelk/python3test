#-*- coding: UTF-8 -*- 
import random

weight1, price1 = eval(input("1. enter weight and price: "))
weight2, price2 = eval(input("2. enter weight and price: "))

if price1/weight1 <= price2/weight2:
	print("the first bag of rice", price1/weight1)
else:
	print("the second bag of rice", price2/weight2)
	
print("1 bag:", price1/weight1, "2 bag:",price2/weight2)	
	
