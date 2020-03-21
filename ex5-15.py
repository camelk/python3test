#-*- coding: UTF-8 -*- 

n = 1
while n != 0:
	n = n + 1
	if n*n*n < 12000:
		continue
	else:
		n = n -1
		break
		
print(n)
