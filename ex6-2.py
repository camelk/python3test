#-*- coding: UTF-8 -*- 

def sumDigits(n):
	sum = 0
	
	while(n != 0):
		remainder = n % 10
		sum = sum + remainder
		n = n // 10
		
	return sum
		
	
	
	
def main():
	
	number = eval(input("Enter the number: "))
			
	print(sumDigits(number))
	
main()
	
