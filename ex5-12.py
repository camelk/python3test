#-*- coding: UTF-8 -*- 


count = 0
for m in range(100, 201):
	if (m % 5 == 0 or  m % 6 == 0):
		print(m, end=" ")
		count = count + 1
		if count % 10 == 0:
			print()
		
print()
