#-*- coding: UTF-8 -*- 

# Get the amount of fund
amount = eval(input("Total amount(ex. 112255): "))

remainingAmount = amount

# no of 1000 bills
numberOfOnethousands = remainingAmount // 1000
remainingAmount = remainingAmount % 1000

# no of 500 bills
numberOfFivehundreds = remainingAmount // 500
remainingAmount = remainingAmount % 500

# no of 100 bills
numberOfOnehundreds = remainingAmount // 100
remainingAmount = remainingAmount % 100

# no of 50 bills
numberOfFifities = remainingAmount // 50
remainingAmount = remainingAmount % 50

# no of 10 bills
numberOfTens = remainingAmount // 10
remainingAmount = remainingAmount % 10

# no of 10 bills
numberOfOnes = remainingAmount

print("Input amount:", amount,"won\n",
		"\t thousands", numberOfOnethousands,"EA\n",
		"\t five hundreds", numberOfFivehundreds,"EA\n",
		"\t one hundres", numberOfOnehundreds,"EA\n",
		"\t fifties", numberOfFifities,"EA\n",
		"\t tens", numberOfTens,"EA\n",
		"\t ones", numberOfOnes,"EA\n")

print(format(57.465895,"10.2f"))
print(format(12345657.465,"10.2f"))
print(format(57.4,"10.2f"))
print(format(57.465895,"10.2f"))
print(format(57,"10.2f"))

print(format(57.465895,"<10.2f"))
print(format(12345657.465,"<10.2f"))
print(format(57.4,"<10.2f"))
print(format(57.465895,"<10.2f"))
print(format(57,"<10.2f"))


print(format(57.465895,"10.2e"))
print(format(12345657.465,"10.2e"))
print(format(57.4,"10.2e"))
print(format(57.465895,"10.2e"))
print(format(57,".2e"))


print(format(57.465895,"10.2%"))
print(format(12345657.465,"10.2%"))
print(format(57.4,"10.2%"))
print(format(57.465895,"10.2%"))
print(format(57,".2%"))

print(format(57,"10d"))
print(format(57,"10x"))
print(format(57,"10o"))
print(format(57,"10b"))

