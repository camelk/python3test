#-*- coding: UTF-8 -*- 
# the name of program module: usefulTurtleFunctions.py
import turtle


# printMonth stub
def drawLine(x1, y1, x2, y2):
	#print("drawLine")
	turtle.penup()
	turtle.goto(x1,y1)
	turtle.pendown()
	turtle.goto(x2,y2)
	
# writeText stub
def writeText(s, x, y):
	#print("writeText")
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.write(s)
	
# drawPoint stub
def drawPoint(x, y):
	#print("drawPoint")
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(3)
	turtle.end_fill()
	
# drawCircle stub
def drawCircle(x = 0, y = 0, radius = 10):
	#print("drawCircle")
	turtle.penup()
	turtle.goto(x,y-radius)
	turtle.pendown()
	turtle.circle(radius)
		
# drawRectangle stub
def drawRectangle(x = 0, y = 0, width = 10, height = 10):
	#print("drawRectangle")
	turtle.penup()
	turtle.goto(x+width/2, y+height/2)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(height)
	turtle.right(90)
	turtle.forward(width)
	turtle.right(90)
	turtle.forward(height)
	turtle.right(90)
	turtle.forward(width)
	

