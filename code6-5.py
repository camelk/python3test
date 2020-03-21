#-*- coding: UTF-8 -*- 
'''
def main():
	i = 1
	while i <= 6:
		print(function1(i,2))
		i += 1
		
def function1(i,num):
	line = " "
	for j in range(1, i):
		line += str(num) + " "
		num *= 2
	return line
	

main()
'''
'''
def main():
	times = 3
	print("before func call, var",
		"times: ", times)
		
	nPrint("welcome to CS!", times)
	
	print("after func call, var",
		"times: ", times)
	
def nPrint(message, n):
	while n > 0:
		print("n = ", n)
		print(message)
		n -= 1
		
main()
'''
def main():
	i = 1
	while i <= 4:
		function1(i)
		i += 1
		
		print("i is ", i, ".")
		
def function1(i):
	line = " "
	while i >= 1:
		if i % 3 != 0:
			line += str(i) + " "
			i -= 1
	
	print(line)
	
main()
		
