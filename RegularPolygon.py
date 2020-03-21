#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  RegularPolygon.py
#  
#  Copyright 2020 root <root@ken>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import math

class RegularPolygon:
	def __init__(self, n = 3, side = 1.0, x = 0.0, y = 0.0):
		self.__n = n
		self.__side = side
		self.__x = x
		self.__y = y
		
	def getN(self):
		return self.__n
		
	def getSide(self):
		return self.__side
		
	def getX(self):
		return self.__x
		
	def getY(self):
		return self.__y
		
	def setN(self, n):
		self.__n = n
		
	def setSide(self, side):
		self.__side = side
		
	def setX(self, x):
		self.__x = x
		
	def setY(self, y):
		self.__y = y
		

	def getPerimeter(self):
		return (self.__n * self.__side)
		
	def getArea(self):
		area = (self.__n * self.__side**2)/(4 * math.tan(math.pi/self.__n))
		return area
