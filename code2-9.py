#-*- coding: UTF-8 -*- 

# enter the year rate in percentage %
x1, y1 = eval(input("Enter the first point (x, y):"))
x2, y2 = eval(input("Enter the second point (x, y):"))

# calculate the distance
distance = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5

# show the result
print("the distance between the two points:", distance)

