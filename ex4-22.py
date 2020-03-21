#-*- coding: UTF-8 -*- 
import math

x1, y1 = eval(input("Enter any point(x,y)(ex. x, y): "))

print("the point", x1, ",", y1)

# define the circle(x0, y0, radius)
x0 = 0
y0 = 0
radius = 10

length = math.sqrt((x0-x1)**2+(y0-y1)**2)

print("length", format(length, ".2f"))

if radius >= length:
	print("the point is within the bound of circle")
else:
	print("the point is out of the bound of circle")


