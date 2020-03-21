#-*- coding: UTF-8 -*- 

a, b, c = eval(input("enter the a, b, c of equeation coefficient:"))

print("a, b, c", a, b, c)

# solution

discriminant = b**2-4*a*c

if discriminant > 0:
	r1 = (-b+(discriminant)**0.5)/2*a
	r2 = (-b-(discriminant)**0.5)/2*a
	print("two real root:", r1, r2)
elif discriminant ==0:
	r = b/2*a
	print("an equal root:", r)
else:
	print("an imaginary root")
	
