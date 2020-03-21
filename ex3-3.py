#-*- coding: UTF-8 -*- 
import math

# enter the lat and long of the each for two points
x1, y1 = eval(input("enter the firt point of earth(ex, 36.5 -25):"))
x2, y2 = eval(input("enter the second point of earth(ex, 36.5 -25):"))

# the greate circle distance
radius = 6370.01 # [km]
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

d = radius*math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(y1-y2))


print("the greate circle distance of the circle distance:", d)
