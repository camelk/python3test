#-*- coding: UTF-8 -*- 


# 1. find divisor
number = eval(input("Enter the ingeger number(1-100):"))
result = 1
for k in range(2, number+1):
	if number % k == 0:
		print("divisor: ", k)
		
		count = 0
		for j in range(2, k+1):
			if k % j == 0:
				count += 1
		
		if count == 1:
			print("prime: ", k)
			while(result < number):
				result*= k
				if result >= number:
					break
				print("reault:", result, ".....", k)
				
				
				
		
		
		
# 2. find out prime number among divsors
# 3. sort the prime number in increasing order


