#-*- coding: UTF-8 -*- 
import turtle

x1, y1 = eval(input("enter the center of circle (x1, y1):"))
radius = eval(input("enter the radius of circle(r):"))
x2, y2 = eval(input("enter any point(x2, y2):"))

# draw the circle
turtle.penup()
turtle.goto(x1,y1-radius)
turtle.pendown()
turtle.circle(radius)

# draw the point
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(3)
turtle.end_fill()

# show the result
turtle.penup()
turtle.goto(x1 - 70, y1-radius-20)
turtle.pendown()

d = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5
if d <= radius:
	turtle.write("the point is in the circle.")
else:
	turtle.write("the point is out of the circle.")
	
turtle.hideturtle()

turtle.done()


