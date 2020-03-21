#-*- coding: UTF-8 -*- 

year = eval(input("enter a year:"))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(year," is the leap year?", isLeapYear)
