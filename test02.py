#-*- coding: UTF-8 -*- 

def main():
	a = A(5)
	print("a ..", a.getA())
	
class A:
	def __init__(self,i=0):
		self.__i = i
		
	def getA(self):
		return self.__i
		
main()
	

	
	
