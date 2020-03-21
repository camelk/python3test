#-*- coding: UTF-8 -*- 
import math

# enter the radius of the area of pentagon

r = eval(input("enter the radius of a pentagon:"))

# the side length of pentagon
s = 2*r*math.sin(math.pi/5)

# forulation to calcualte the area of the pentagon
area = (3*math.sqrt(3))/2*(s**2)

print("the area of the pentagon:", area)
