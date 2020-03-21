#-*- coding: UTF-8 -*- 


def displaySortedNumbers(num1, num2, num3):
	#print("sortedNumbers")
	if num1 > num2:
		num1, num2=num2,num1
		
	if num1 > num3:
		num1, num3=num3,num1
		
	if num2 > num3:
		num2, num3=num3,num2
	
	print(num1, num2, num3)

def main():
	n1, n2, n3 = eval(input("enter the numbers of the three: "))
	displaySortedNumbers(n1,n2,n3)
	
	
main()
