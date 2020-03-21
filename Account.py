#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Account.py
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


class Account:
	def __init__(self, id =0, balance = 100000, annualInterestsRate = 0):
		self.__id = id
		self.__balance = balance
		self.__annualInterestsRate = annualInterestsRate / 100
	
	def getId(self):
		return self.__id
		
	def getBalance(self):
		return self.__balance
		
	def getAnnualInteresetsRate(self):
		return self.__annualInterestsRate
		
	def setId(self, id):
		self.__id = id
		
	def setBalance(self, balance):
		self.__balance = balance
		
	def setAnnualInterestsRate(self, annualInterestsRate):
		self.__annualInterestsRate = annualInterestsRate /100
		
	def getMonthlyInterestRate(self):
		return self.__annualInterestsRate / 12 * 100
		
	def getMonthlyInterest(self):
		return self.__balance * self.getMonthlyInterestRate()
		
	def withdraw(self, amount):
		self.__balance -= amount
		return amount
		
	def deposit(self, amount):
		self.__balance += amount





