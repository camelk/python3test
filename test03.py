#-*- coding: UTF-8 -*- 

def main():
	a = A(False)
	print(a.getOn())
	
class A:
	def __init__(self, on = False):
		self.__on = not on
		
	def getOn(self):
		return self.__on
	
main()
