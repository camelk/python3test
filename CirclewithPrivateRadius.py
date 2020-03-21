#-*- coding: UTF-8 -*- 
import math as m

class Circle:
	def __iniit__(self, radius = 1):
		self.__radius = radius
		
	def getRadius(self): # getter, accessor
		return self.__radius
		
	def getPerimeter(self): #getter, accessor
		return 2 * self.__radius * m.pi
		
	def getArea(self):
		return self.__radius * self.__radius * m.pi
		
