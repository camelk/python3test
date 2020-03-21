#-*- coding: UTF-8 -*- 

def reverse(num):
	print(num)

	return rnum # retrun reverse number
		
	
def isPalindrome(num):
	rnum = reverse(num)
	return (num == rnum)
		
def main():
	
	number = eval(input("Enter the number: "))
	
	if(isPalindrome(number)):
		print("the Palindrome is a", number)
	else:
		print("the Palindrome is not a", number)
	
	
main()
	
