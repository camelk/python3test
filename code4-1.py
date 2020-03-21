#-*- coding: UTF-8 -*- 
import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)

answer = eval(input(str(number1) + "+" + str(number2) + "=?:"))

print(number1, "+", number2, "=", answer, "quiz:", number1+number2==answer)

