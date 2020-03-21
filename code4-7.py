#-*- coding: UTF-8 -*- 
import sys

status = eval(input("0 - single filer\n" + \
					"1 - married filing joinly\n" +  \
					"2 - married filing seperatly\n" + \
					"4 - head of househod\n" + 
					" which filer do you select? "))

income = eval(input("enter your taxable inocme ? "))

tax = 0

if status == 0:
	if income <= 8350:
		tax = income * 0.10		
	elif income <= 33950:
		tax = 8835 * 0.10 + (income-8350) * 0.15
	elif income <= 82250:
		tax = 8835 * 0.10 + (33950 * 0.15) + (income -33950) * 0.15
	elif income <= 171550:
		tax = 8835 * 0.10 + (33950 - 8530) * 0.15 + (88250 - 33950) * 0.25 + (income - 88250) * 0.28
	elif income <= 372950:
		tax = 8835 * 0.10 + (33950 - 8530) * 0.15 + (88250 - 33950) * 0.25 + (171550 - 88250) * 0.28 + \
		(income - 171550) * 0.33
	else:
		tax = 8835 * 0.10 + (33950 - 8530) * 0.15 + (88250 - 33950) * 0.25 + (171550 - 88250) * 0.28 + \
		(372950 - 171550) * 0.33 + (income - 372950)
elif status == 1:
	printf("------")
elif status == 2:
	printf("------")
elif status == 3:
	printf("------")
else:	
	printf("------")
	sys.exit()
	
print("tax: ", format(tax, ".2f"))

		
