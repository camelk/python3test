#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex7-3.py
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

from Account import Account

def main():
	sevenAccount = Account(1122, 20000000, 4.5) # yearRate-> 4.5%
	
	debit = sevenAccount.withdraw(2500000)
	sevenAccount.deposit(3000000)
	
	print("account debit: ", debit)
	print("account number: ", sevenAccount.getId())
	print("account balance ", sevenAccount.getBalance())
	print("monthly interests rate: ", sevenAccount.getMonthlyInterestRate(),"%")
	print("monthly interest: ", sevenAccount.getMonthlyInterest())
	
main()
