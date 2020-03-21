#-*- coding: UTF-8 -*- 
# check the prime number?
def isPrime(number):
	divisor = 2
	while divisor <= number / 2:
		if number % divisor == 0:
			return False # not prime number
		divisor += 1
		
	return True
	
def printPrimeNumbers(numberOfPrimes):
	NUMBER_OF_PRIMES = 50
	NUMBER_OF_PRIMES_PER_LINE = 10
	
	count = 0
	number = 2
	
	while count < numberOfPrimes:
		if isPrime(number):
			count += 1
			print(number, end=" ")
			if count % NUMBER_OF_PRIMES_PER_LINE == 0:
				print()
			
		number += 1
		
def main():
	print("the first 50 of prime numbers")
	printPrimeNumbers(50)
	
main()


	
	
