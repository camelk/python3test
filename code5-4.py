#-*- coding: UTF-8 -*- 
import random
import time

correctCount = 0
count = 0
NUMBER_OF_QUESTIONS = 5

startTime= time.time() # get the start time

while count < NUMBER_OF_QUESTIONS:
	number1 = random.randint(1,100)
	number2 = random.randint(1,100)
	answer = eval(input(str(number1) + "-" + str(number2) + "="))
	
	if number1 - number2 == answer:
		print("Successful")
		correctCount += 1
	else:
		print("Wrong")

	count += 1

endTime = time.time()
testTime = int(endTime - startTime)

print("the No. of Correct Answer:", correctCount)
print("Calcuting Time: ", testTime,"[sec]")


	
	

