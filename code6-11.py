#-*- coding: UTF-8 -*- 
from random import randint

# crate a random charater between ch1 to ch2
def getRandomCharacter(ch1, ch2):
	return chr(randint(ord(ch1), ord(ch2)))
	
def getRadnomLowerCaseLetter():
	return chr(randint(ord('a'), ord('z')))
	
def getRadnomUpperCaseLetter():
	return chr(randint(ord('A'), ord('Z')))
	
def getRadnomDigitCharacter():
	return chr(randint(ord('0'), ord('9')))
	
def getRadnomASCIICharacter():
	return chr(randint(0,127))
