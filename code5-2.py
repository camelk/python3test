#-*- coding: UTF-8 -*- 
import random


number = random.randint(0,100)


print("Why don't you enter a magic number between 0 and 100:")

guess = -1
while guess != number:
	guess = eval(input("Enter a magic number:"))
	if guess == number:
		print("successful", number)
	elif guess > number:
		print("less than the guess")
	else:
		print("more than the guess")
