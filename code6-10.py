#-*- coding: UTF-8 -*- 

def sort(number1, number2):
	if number1 < number2:
		return number1, number2
	else:
		return number2, number1

n1,n2 = sort(30,40)
print("n1: ", n1)
print("n2: ", n2)
