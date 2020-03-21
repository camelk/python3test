#-*- coding: UTF-8 -*- 

tuition = 1000

year = 0

while tuition < 2000:
	#tuition = tuition + tuition * 0.07
	tuition = tuition * 1.07
	year += 1

print(format(tuition,".2f"), year)
