#-*- coding: UTF-8 -*- 
def decimalToHex(decimalValue):
	hex = ""
	
	while decimalValue != 0:
		hexValue = decimalValue % 16
		hex = toHexChar(hexValue) + hex
		decimalValue = decimalValue // 16
		
	return hex
	
def toHexChar(hexValue):
	if 0 <= hexValue <= 9:
		return chr(hexValue + ord('0'))
	else:
		return chr(hexValue - 10 + ord('A'))
		
def main():
	decimalValue = eval(input("enter a number: "))
	
	print("decimalValue: ", decimalValue, decimalToHex(decimalValue))
	
main()

		
