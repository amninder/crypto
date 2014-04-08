from random import *
import time
import gmpy2
from gmpy2 import *
import mersenne_twistter

def primalityTest(n, k):
	if n<2:
		return False
	if n % 2==0:
		return False

	s = 0
	d = n-1

	while d % 2 ==0:
		s += 1
		d >>= 1
	for i in range(k):
		rand = randint(2, n-2)
		# from datetime import datetime
		# rand = mersenne_twistter.retRandom(datetime.now().second)
		# x = (rand**d) % n
		x = powmod(rand, d, n)
		# x = t_divmod(rand**d, n)
		if x==1 or x==n-1:
			continue
		for r in range(s):
			toReturn = True
			x = powmod(x, 2, n)
			if x==1:
				return False
			if x==n-1:
				toReturn = False
				break
		if toReturn:
			return False
	return True

"""
	returns prime number based upon time as seed
"""
from datetime import datetime

def seed():
	return mersenne_twistter.retRandom(datetime.now().microsecond)

def _getRandomNumber():
	num = seed()
	if primalityTest(num, 1):
		return num
	else:
		return _getRandomNumber()

def _isPrime(num):
	if primalityTest(num, 1):
		return True
	else:
		return False

def getDigits(num):
	i = 0
	while num>0:
		i += 1
		num /= 10
	return i
