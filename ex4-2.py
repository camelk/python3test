#-*- coding: UTF-8 -*- 
import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)

answer = eval(input(str(number1) + "+" + str(number2) + "+" + str(number3) + "= "))


print(number1, "+", number2, "+", number3, "=", answer)

	
