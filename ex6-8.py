#-*- coding: UTF-8 -*- 

def celsiusToFahrenheit(celsius):
	#print("celsiusToFahrenheight")
	return (9/5) * (celsius - 32)
	
	
def fahrenheitToCelius(fahrenheit):
	#print("fahrenheightToCelius")
	return (5/9) * (fahrenheit + 32)
	
	
def main():
	print("Celsius\t", "Farenheit", "|", "Farenheiht\t", "Celsius")
	
	for i in range(40, 29, -1):
		print(i, "\t", format(celsiusToFahrenheit(i), ">8.2f"))
	for j in range(120, 29, -10):
		print(j, "\t", format(fahrenheitToCelius(j), ">8.2f"))
	
main()
