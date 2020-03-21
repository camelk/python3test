#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex7-5.py
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

from RegularPolygon import RegularPolygon

def main():
	p1 = RegularPolygon()
	
	print("Polygon 1 Area:", format(p1.getArea(),"10.2f"))
	print("Polygon 1 Perimeter:", format(p1.getPerimeter(), "5.2f"))
	print()
	
	p2 = RegularPolygon(6, 4)
	
	print("Polygon 2 Area:", format(p2.getArea(),"10.2f"))
	print("Polygon 2 Perimeter:", format(p2.getPerimeter(), "5.2f"))
	print()
	
	p3 = RegularPolygon(10, 4, 5.6, 7.8)
	
	print("Polygon 3 Area:", format(p3.getArea(),"10.2f"))
	print("Polygon 3 Perimeter:", format(p3.getPerimeter(), "5.2f"))
	print()
	
main()
