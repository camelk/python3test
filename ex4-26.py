#-*- coding: UTF-8 -*- 
import random


number = eval(input("Enter the interger of 3 in size):"))
#print(number)

first = number //100
second = number % 10
#print(first, second)

if first == second:
	print("this number is a palindrome:", number)
else:
	print("this number is not a palindrome:", number)
	
