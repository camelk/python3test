#-*- coding: UTF-8 -*- 

a = ord('!')
b = ord('~')
count = 0
for i in range(a, b):
	print(chr(i),end=" ")
	count += 1
	if count % 10 == 0:
		print()
