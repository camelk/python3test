#-*- coding: UTF-8 -*- 
import RandomCharacter

NUMBER_OF_CHARS = 175
CHARS_PER_LINE = 25

for i in range(NUMBER_OF_CHARS):
	print(RandomCharacter.getRadnomLowerCaseLetter(), end="")
	if (i+1) % CHARS_PER_LINE == 0:
		print()
