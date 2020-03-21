#-*- coding: UTF-8 -*- 
import math

print("degree	 sin	    cos")
for deg in range(0, 360, 10):
	rad = math.degrees(deg)
	print(format(deg, "<4d"), \
		format(math.sin(rad),"10.4f"), \
		format(math.cos(rad),"10.4f"))
	
