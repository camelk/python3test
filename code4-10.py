#-*- coding: UTF-8 -*- 
import random

lottery = random.randint(0,99)

guess = eval(input("enter the 2 numbers for lotter:"))

lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("lottery number:", lottery)

if guess == lottery:
	print("You got 10,000,000won")
elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
	print("You got 3,000,000won")
elif (guessDigit1 == lotteryDigit1
		or guessDigit1 == lotteryDigit2
		or guessDigit2 == lotteryDigit1
		or guessDigit2 == lotteryDigit2):
	print("You got 1,000,000won")
else:
	print("You failed to win the lottery")


