#-*- coding: UTF-8 -*- 
import turtle

# enter the year rate in percentage %
x1, y1 = eval(input("Enter the first point (x, y):"))
x2, y2 = eval(input("Enter the second point (x, y):"))

# calculate the distance
distance = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5

# show the result
# print("the distance between the two points:", distance)

# draw the line connected between the two points
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("Point one")
turtle.goto(x2,y2)
turtle.write("Point two")

# mvoe to the center point of the line
turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.write(int(distance))

turtle.done()

