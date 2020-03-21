#-*- coding: UTF-8 -*- 

stuNo = eval(input("enter the number of students: "))

max1 = 0
max2 = 0
for i in range(0, stuNo):
	score = eval(input("enter the score of a student: "))
	if max1 < score:
		temp = max1
		max1 = score		
		if max2 < temp:
			max2 = temp
	
	print(max1, max2)
	print(i)
	
print("max1: ", max1, "max2: ", max2)
