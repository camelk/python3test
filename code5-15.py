#-*- coding: UTF-8 -*- 
import turtle
from random import randint

turtle.speed(2)

turtle.color("gray")

x = -80

for y in range(-80, 80+1, 10):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.forward(160)
	
y = 80
turtle.right(90)

for x in range(-80, 80+1, 10):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.forward(160)	

turtle.pensize(3)
turtle.color("red")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

x=y=0
while abs(x) < 80 and abs(y) < 80:
	r = randint(0,3)
	if r == 0: # right
		x += 10
		turtle.setheading(0)
		turtle.forward(10)
	elif r == 1: # down
		y -= 10
		turtle.setheading(270)
		turtle.forward(10)
	elif r == 2: # left
		x -= 10
		turtle.setheading(180)
		turtle.forward(10)
	elif r == 3: # upward
		y += 10
		turtle.setheading(90)
		turtle.forward(10)
	'''else:
		print("diection error")'''
turtle.done()