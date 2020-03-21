#-*- coding: UTF-8 -*- 
import math

RATE_PER_YEAR = 0.05 # 1 + 0.5
tuition = 100 #[10thansands]

amount = 0
bmount = 0
temp = 0

for k in range(0,4):
	rate = k * tuition * RATE_PER_YEAR
	tuition = tuition + rate
	amount += tuition
	print(k+1, "year.......tution fee;", format(tuition,"10.2f"))
print("total: --------------------------",format(amount,"10.2f"))
	
tuition = 100 #[10thansands]
for i in range(0,1):
	rate = i * tuition * RATE_PER_YEAR
	temp = tuition + rate
	bmount += tuition
	print(k+1, "year.......tution fee;", format(tuition,"10.2f"))


		
	
	
