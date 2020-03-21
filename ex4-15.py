#-*- coding: UTF-8 -*- 
import random

lottery = random.randint(0,999)

guess = eval(input("enter the 3 numbers for lotter:"))

lotteryDigit1 = lottery // 100
lotteryDigit2 = lottery % 100 // 10
lotteryDigit3 = lottery % 10

guessDigit1 = guess // 100
guessDigit2 = guess % 100 // 10
guessDigit3 = guess % 10


print("lottery number:", lottery)

if guess == lottery:
	print("You got 10,000,000won")
elif (guessDigit2 == lotteryDigit3 
		and guessDigit3 == lotteryDigit1 
		and guessDigit1 == lotteryDigit2
		and guessDigit2 == lotteryDigit1
		and guessDigit3 == lotteryDigit2
		and guessDigit1 == lotteryDigit3
		):
	print("You got 3,000,000won")

elif (guessDigit1 == lotteryDigit1
		or guessDigit1 == lotteryDigit2
		or guessDigit1 == lotteryDigit3
		or guessDigit2 == lotteryDigit1
		or guessDigit2 == lotteryDigit2
		or guessDigit2 == lotteryDigit3
		or guessDigit3 == lotteryDigit1
		or guessDigit3 == lotteryDigit2
		or guessDigit3 == lotteryDigit3):
	print("You got 1,000,000won")

else:
	print("You failed to win the lottery")



