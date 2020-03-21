#-*- coding: UTF-8 -*- 

data = eval(input("enter the number fo integer: "))
print(data)
max = 0
while (data != 0):
	data = eval(input())
	if max < data:
		max = data
	
	
print("max:", max)
