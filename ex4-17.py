#-*- coding: UTF-8 -*- 
import random

quiz = random.randint(0,2)
answer = eval(input("enter the scissor(0), rock(1), paper(2):"))

if answer == 0:
	if quiz == 2:
		print("user wined", "computer:", quiz, "user:", answer)
	elif quiz == 1:
		print("user lost", "computer:", quiz, "user:", answer)
	else:
		print("user is tied", "computer:", quiz, "user:", answer)
elif answer == 1:
	if quiz == 0:
		print("user wined", "computer:", quiz, "user:", answer)
	elif quiz == 2:
		print("user lost", "computer:", quiz, "user:", answer)
	else:
		print("user is tied", "computer:", quiz, "user:", answer)
else: # answer == 2:
	if quiz == 1:
		print("user wined", "computer:", quiz, "user:", answer)
	elif quiz == 0:
		print("user lost", "computer:", quiz, "user:", answer)
	else:
		print("user is tied", "computer:", quiz, "user:", answer)
		


