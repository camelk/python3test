#-*- coding: UTF-8 -*- 


countPositive = 0
countNegative = 0
totalSum = 0
average = 0
inputCount = 0;

number = eval(input("enter an interger number(if quit, 0:)"))

while number != 0:
	if number == 0:
		break;
	elif number > 0:
		countPositive += 1
	elif number < 0:
		countNegative += 1
	
	inputCount += 1
	totalSum += number
	
	number = eval(input("enter an interger number(if quit, 0:"))

if totalSum == 0:
	print("total sum is 0")
else:
	average = totalSum / inputCount
	print("+number:", countPositive)
	print("-number:", countNegative)
	print("total sum:", totalSum)
	print("average:", average)
		
