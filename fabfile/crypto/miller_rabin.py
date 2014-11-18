# coding=utf-8
from random import *
from gmpy2 import *
"""
http://en.wikipedia.org/wiki/Miller–Rabin_primality_test

Input: n > 3, an odd integer to be tested for primality;
Input: k, a parameter that determines the accuracy of the test
Output: composite if n is composite, otherwise probably prime

write n − 1 as 2s·d with d odd by factoring powers of 2 from n − 1

WitnessLoop: repeat k times:
   pick a random integer a in the range [2, n − 2]
   x ← a^d mod n
   if x = 1 or x = n − 1 then do next WitnessLoop
   repeat s − 1 times:
      x ← x^2 mod n
      if x = 1 then return composite
      if x = n − 1 then do next WitnessLoop
   return composite
return probably prime

"""
def millerRabin(n, k=3):
	if n<2:
		return False
	if n%2==0:
		return False

	s = 0
	d = n-1

	while d%2==0:
		s 	+=	1
		d 	>>=	1
	for i in range(k):
		rand 	= randint(2, n-2)
		x 		= powmod(rand, d, n)
		if x == 1 or x == n-1:
			continue
		for r in range(s):
			isPrime = True
			x = powmod(x,2,n)
			if x==1:
				return False
			if x==n-1:
				isPrime = False
				break
		if isPrime:
			return False
	return True