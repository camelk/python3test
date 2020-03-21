#-*- coding: UTF-8 -*- 
import turtle as t
import math as m
x1, y1, x2, y2, x3, y3 = eval(input("Ehtner three points(ex. 1,2,...):"))

t.penup()
t.goto(x1,y1)
t.write("p1")
t.pendown()
t.goto(x2,y2)
t.write("p2")
t.goto(x3,y3)
t.write("p3")
t.goto(x1,y1)

#t.write("p1(",x1,",",y1,")")
#t.write("p2(",x2,",",y2,")")
#t.write("p3(",x3,",",y3,")")

s1 = m.sqrt((x2-x1)**2+(y2-y1)**2)
s2 = m.sqrt((x3-x2)**2+(y3-y2)**2)
s3 = m.sqrt((x1-x3)**2+(y1-y3)**2)
s = (s1+s2+s3)/2
area = m.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print("area = ", area)

t.hideturtle()
t.done()

