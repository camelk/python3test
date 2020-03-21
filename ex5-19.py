#-*- coding: UTF-8 -*- 


num = eval(input("enter the number(1-15): "))


temp = 1
while(num):
	for i in range(1,num):
		print("  ", end="  ")
	
	for k in range(temp, 0, -1):
		print(format(k,"2d"), end="  ")	
	
	for k in range(2, temp+1, 1):
		print(format(k,"2d"), end="  ")	
	
	for i in range(1,num):
		print("  ", end="  ")
	num -= 1
	temp +=1
	print()


