#-*- coding: UTF-8 -*- 
import random

choice = eval(input("KRW->CNY: 0, CNY->KRW: 1:"))

if choice == 0: # KRW
	KRWperCNY = eval(input("exchange of rate: 100KRW --> KRW:"))	
	krw = eval(input("enter the amount of KRW:"))
	cny = krw/100 * 0.59
	print("KRW: ", krw, "==> CNY: ", cny)
else: # unit == 1 CNY
	KRWperCNY = eval(input("exchange of rate: CNY --> KRW:"))
	cny = eval(input("enter the amount of CNY:"))
	krw = cny * 170.4
	print("KRW: ", krw, "==> CNY: ", cny)
	
