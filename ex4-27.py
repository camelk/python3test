#-*- coding: UTF-8 -*- 
import random

print("the coordinates of triangel")

x0, y0, x1, y1, x2, y2 = 0, 0, 200, 0, 0, 100

print(x2, y2)

x, y = eval(input("enter a position(x,y): "))

maxy = -0.5*x +100

print(y)
if x0 <= x <= x1 and y0 <= y <= maxy:
	print("be in the triangle")
	
else:
	print("be out of the triangle")

