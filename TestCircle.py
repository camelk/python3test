#-*- coding: UTF-8 -*- 
from Circle import Circle

def main():
	c1 = Circle()
	print("Radius: ", c1.radius, "Circle1 Area:", c1.getArea())
	
	c2 = Circle(25)
	print("Radius: ", c2.radius, "Circle2 Area:", c1.getArea())
	
	c3 = Circle(125)
	print("Radius: ", c3.radius, "Circle3 Area:", c1.getArea())

	c2.radius = 100
	print("Radius: ", c2.radius, "Circle2 Area:", c2.getArea())
	
	c1.setRadius(50)
	print("Radius: ", c1.radius, "Circle1 Area:", c1.getArea())

main()
