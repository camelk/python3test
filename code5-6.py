#-*- coding: UTF-8 -*- 

print("		multiplication table")

print("|", end='')
for j in range(1,10):
	print(" ", format(j,"3d"),end='')
print()
print("-----------------------------------------------")
for i in range(1,10):
	print(i,"|",end='')
	for j in range(1, 10):
		print(format(i*j, "4d"), end=' ')
	print()
	


