#-*- coding: UTF-8 -*- 
import random

kgPerPound = 0.45359237
meterPerInch = 0.0254
meterPerFeet = 0.3048

pound = eval(input("what is your weight? [pound]:"))
feet, inch = eval(input("what is your hight? [0 feet, 0 inch]: "))

weight = pound * kgPerPound
height = feet * meterPerFeet + inch * meterPerInch
print("your weight:", format(weight,".2f"), "[kg] and height: ", format(height,".2f"),"[m].")

bmi = weight / (height**2)

if bmi < 18.5:
	print("BMI: ", format(bmi,".2f"), "your are low weight")
elif bmi < 25:
	print("BMI: ", format(bmi,".2f"), "normal weight")
elif bmi < 30:
	print("BMI: ", format(bmi,".2f"), "over weight")
else: # bmi >= 3.0
	print("BMI: ", format(bmi,".2f"), "obesity")

