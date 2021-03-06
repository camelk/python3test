#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Fan.py
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

class Fan:
	def __init__(self, speed, on, radius, color):		
		self.__speed = speed
		self.__on = on
		self.__radius = radius
		self.__color = color
		
	def getSpeed(self):
		SLOW = 1
		MEDIUM = 2
		FAST = 3
		
		return self.__speed
		
	def getOn(self):
		return self.__on
		
	def getRadius(self):
		return self.__radius
		
	def getColor(self):
		return self.__color
		
	def setSpeed(self, speed):
		self.__speed = speed
		
	def setOn(self, on):
		self.__on = on
		
	def setRadius(self, radius):
		self.__radius = radius
		
	def setColor(self, color):
		self.__color = color
		
