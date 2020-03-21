#-*- coding: UTF-8 -*- 
import math

x1, y1 = eval(input("Enter any point(x,y)(ex. x, y): "))

print("the point", x1, ",", y1)

# define the rectangle(0, y0, width, height)
x0 = 0;
y0 = 0;
width = 10
height = 5

if width/2 >= math.fabs(x1) and height/2 >= math.fabs(y1):
	print("the point is within the bound of the rectangle")
else:
	print("the point is out of the bound of the rectangle")


