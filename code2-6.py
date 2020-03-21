#-*- coding: UTF-8 -*- 

# enter integer variable from a user
purchaseAmount = eval(input("input total buy amount: "))

# calculate the sales taxes
tax = purchaseAmount * 0.06

# show the result [0.xx]
print("Salse Tax: ", int(tax*100)/100.0)
