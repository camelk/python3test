#-*- coding: UTF-8 -*- 

sum = 0.0

i = 0.01
count = 0

while count < 100:
	sum += i
	i = i + 0.01
	count += 1
	
print(sum)
