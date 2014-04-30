import RSA
import miller_rabin
from gmpy2 import *
import gmpy2

def plotTime(p):
	n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	while not miller_rabin.millerRabin(n, 2):
		n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	print ("number: %d and bit: %d"%(n, bit_length(n)))

total_primes = []
nextP = 1
def nextPrime(p):
	power = 100
	global total_primes
	global nextP
	while nextP <= p:
		nextP = next_prime(nextP)
		total_primes.append(nextP)
	return len(total_primes)-1
	

def primeRange(j):
	x = 1
	range = []
	tot_primes = []
	while x <=j:
		print ("%d in %d"%(nextPrime(x), x))
		range.append(x)
		tot_primes.append(float(nextPrime(x))/float(x))
		x *= 10
	return (range, tot_primes)

print primeRange(10000)