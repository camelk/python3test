#-*- coding: UTF-8 -*- 

# enter the year rate in percentage %
annualInterestRate = eval(input("Enter the value (ex, 7.25): "))

monthlyInterestRate = annualInterestRate / 1200

# enter the return year
numberOfYears = eval(input("enter the return year(ex. 5): "))

# enter the loan for a person
loanAmount = eval(input("enter the loan(ex. 1200): "))

# calculate total retun amount
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1/(1 + monthlyInterestRate)**(numberOfYears*12))
totalPayment = monthlyPayment * numberOfYears * 12

# show the result
print("monthly return amount: ", int(monthlyPayment * 100) / 100)
print("total return amount: ", int(totalPayment * 100) / 100)
