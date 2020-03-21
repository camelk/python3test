#-*- coding: UTF-8 -*- 


def displayPattern(n):
	count = n
	while(count):
		print(format(count,"<3d"), end="")
		count = count -1
	print();
	
	k = n
	while(k):
		for j in range(k, 1, -1):
			print(format(" ",">2s"), end=" ")
		for i in range(n-k+1, 0, -1):
			print(format(i, "2d"), end=" ")
		print()
		k = k - 1
		
	

def main():
	num = eval(input("enter the random number: "))
	displayPattern(num)
	
	
main()
