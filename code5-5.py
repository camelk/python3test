#-*- coding: UTF-8 -*- 

data = eval(input("Enter the int number:"))
print("\n")

sum = 0

while data != 0:
	sum += data
	data = eval(input("Enter the int number:"))
	print("\n")
	
print("sum: ", sum)
