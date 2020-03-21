#-*- coding: UTF-8 -*- 
import random


cardNumber = random.randint(1,52)
print("card Number:", cardNumber)

cardKind = cardNumber // 13;
cardOrder= cardNumber % 13;

if cardKind == 0: # clover
	print("cardKind is clover", end=",")
	
	if cardOrder == 0:
		print("card is King")
	elif cardOrder == 1:
		print("card is 1")
	elif cardOrder == 2:
		print("card is 2")
	elif cardOrder == 3:
		print("card is 3")
	elif cardOrder == 4:
		print("card is 4")
	elif cardOrder == 5:
		print("card is 5")
	elif cardOrder == 6:
		print("card is 6")
	elif cardOrder == 7:
		print("card is 7")
	elif cardOrder == 8:
		print("card is 8")
	elif cardOrder == 9:
		print("card is 9")
	elif cardOrder == 10:
		print("card is 10")
	elif cardOrder == 11:
		print("card is J")
	elif cardOrder == 12:
		print("card is Q")
	else:
		print("exception handling")
		
elif cardKind == 1: # diamond	
	print("cardKind is diamond", end=",")
	
	if cardOrder == 0:
		print("card is King")
	elif cardOrder == 1:
		print("card is 1")
	elif cardOrder == 2:
		print("card is 2")
	elif cardOrder == 3:
		print("card is 3")
	elif cardOrder == 4:
		print("card is 4")
	elif cardOrder == 5:
		print("card is 5")
	elif cardOrder == 6:
		print("card is 6")
	elif cardOrder == 7:
		print("card is 7")
	elif cardOrder == 8:
		print("card is 8")
	elif cardOrder == 9:
		print("card is 9")
	elif cardOrder == 10:
		print("card is 10")
	elif cardOrder == 11:
		print("card is J")
	elif cardOrder == 12:
		print("card is Q")
	else:
		print("exception handling")
		
elif cardKind == 2: # heart
	print("cardKind is heart", end=",")
	
	if cardOrder == 0:
		print("card is King")
	elif cardOrder == 1:
		print("card is 1")
	elif cardOrder == 2:
		print("card is 2")
	elif cardOrder == 3:
		print("card is 3")
	elif cardOrder == 4:
		print("card is 4")
	elif cardOrder == 5:
		print("card is 5")
	elif cardOrder == 6:
		print("card is 6")
	elif cardOrder == 7:
		print("card is 7")
	elif cardOrder == 8:
		print("card is 8")
	elif cardOrder == 9:
		print("card is 9")
	elif cardOrder == 10:
		print("card is 10")
	elif cardOrder == 11:
		print("card is J")
	elif cardOrder == 12:
		print("card is Q")
	else:
		print("exception handling")
	
elif cardKind == 3: # spade
	print("cardKind is spade", end=",")
	
	if cardOrder == 0:
		print("card is King")
	elif cardOrder == 1:
		print("card is 1")
	elif cardOrder == 2:
		print("card is 2")
	elif cardOrder == 3:
		print("card is 3")
	elif cardOrder == 4:
		print("card is 4")
	elif cardOrder == 5:
		print("card is 5")
	elif cardOrder == 6:
		print("card is 6")
	elif cardOrder == 7:
		print("card is 7")
	elif cardOrder == 8:
		print("card is 8")
	elif cardOrder == 9:
		print("card is 9")
	elif cardOrder == 10:
		print("card is 10")
	elif cardOrder == 11:
		print("card is J")
	elif cardOrder == 12:
		print("card is Q")
	else:
		print("exception handling")
else:
	print("exception phrase")
