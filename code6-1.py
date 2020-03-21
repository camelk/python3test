#-*- coding: UTF-8 -*- 
'''
def sum(s, t):
	result = 0
	
	for i in range(s, t+1):
		result += i
		
	return result
	
def main():
	print("sum from 1 to 10:", sum(1,10))
	print("sum from 20 to 37:", sum(20,37))
	
	
main()
'''



def max(a, b):
	if a > b:
		result = a
	else:
		result = b
		
	return result
	
def main():
	i = 5
	j = 2
	k = max(i,j)
	print("max value: ", k)
	
main()


	
	
