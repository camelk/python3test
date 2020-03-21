#-*- coding: UTF-8 -*- 
import random


x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter the coordinates(points) of 4:"))

print(x1, y1, x2, y2, x3, y3, x4, y4)

# ax + by = e
# cx + dy = f
# ==> x = (ed-bf)/(ad-bc),  y = (af-ec)/(ad-bc),
# ==> if ad-bc ==0: the two lines are parallel)

a = (y1 - y2)
b = (x1 - x2)
c = (y3 - y4)
d = (x3 - x4)
e = (y1 - y2) * x1 - (x1 - x2)* y1
f = (y3 - y4) * x3 - (x3 - x4)* y3

if (a*d - b*c) == 0:
	print("the two lines are parallel")
else:
	x = (e*d - b*f)/(a*d - b*c)
	y = (a*f - e*c)/(a*d - b*c)
	print("the intersectipn point of two lines:", format(x,".2f"), format(y,".2f"))
