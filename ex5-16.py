#-*- coding: UTF-8 -*- 

n1 = 16
n2 = 24

k = 1
while k <= n1 and k <= n2:
	if n1 % k == 0 and n2 % k ==0:
		gcd = k
	k += 1
	
print("GCD:", gcd)
		

