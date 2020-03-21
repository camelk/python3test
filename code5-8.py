#-*- coding: UTF-8 -*- 

n1 = eval(input("enter the first integer number:"))
n2 = eval(input("enter the second integer number:"))

gcd = 1
k = 2
while k <= n1 and k <= n2:
	if n1 % k == 0 and n2 % k == 0:
		gcd = k
	k += 1
	
print(n1, "and", n2, "has the greatest common divisor", gcd)

