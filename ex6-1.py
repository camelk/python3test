#-*- coding: UTF-8 -*- 

def getPentagonalNumber(n):
	return n*(3*n-1)/2
	
	
def main():
	
	number = 100
	for i in range(1, number+1):
		if getPentagonalNumber(i) > number:
			break
		print(int(getPentagonalNumber(i)), end=" ")
		if (i % 10 == 0):
			print()
		
	print()
	
main()
	
