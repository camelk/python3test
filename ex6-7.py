#-*- coding: UTF-8 -*- 


def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
	#print(investmentAmount, monthlyInterestRate, years)
	months = 12 * years
	monthlyInterestRate = monthlyInterestRate / 100
	futureMoney = investmentAmount * (1 + monthlyInterestRate)**months
	
	return futureMoney
	
	

def main():
	amount = eval(input("Enter Investment Amount: "))
	interest = eval(input("Enter interestRate per year: "))
	
	months = 12
	#years = 30
	for year in range(1,31):
		totalMoney = futureInvestmentValue(amount, interest/months, year)
		print(format(year, "<d"), "\t", format(totalMoney,">15.2f"))
		
	
	
main()
