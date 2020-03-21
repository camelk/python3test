#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex7-4.py
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

from Fan import Fan

def main():
	
	fan1 = Fan(3, 10,"yellow", True)
	fan2 = Fan(2, 5, "blue", False)
	
	print("Fan1................")
	print("Speed: ", fan1.getSpeed())
	print("Power On/Off: ", fan1.getOn())
	print("Fan Radius: ", fan1.getRadius())
	print("Fan Color: ", fan1.getColor())
	
	print("Fan2................")
	print("Speed: ", fan2.getSpeed())
	print("Power On/Off: ", fan2.getOn())
	print("Fan Radius: ", fan2.getRadius())
	print("Fan Color: ", fan2.getColor())

main()
