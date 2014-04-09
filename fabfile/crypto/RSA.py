import miller_rabin
import mersenne
from random import randint
import gmpy2
from gmpy2 import *
from datetime import datetime

		
def seed():
	return datetime.now().microsecond

def getRandomPrime():
	n = mersenne.retRandom(seed())
	if miller_rabin.millerRabin(n, 4):
		return n**2
	else:
		return getRandomPrime()

def getRandom():
	return mersenne.retRandom(seed())

def step2(p, q, r, s):
	_n 		= p*q
	_m 		= r*s
	_phi 	= (p-1) * (q-1)
	_lambda	= (r-1) * (s-1)
	return (_n, _m, _phi, _lambda)


"""Derived from Pseudocode: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Iterative_method_2"""
def extended_gcd(aa, bb):
	lastremainder, remainder = abs(aa), abs(bb)
	x, lastx, y, lasty = 0, 1, 1, 0
	while remainder:
		lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
		x, lastx = lastx - quotient*x, x
		y, lasty = lasty - quotient*y, y
	return lastremainder, lastx * (-1 if aa<0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x%m

"""Euclid's algorithm to find GCD: http://en.wikipedia.org/wiki/Euclidean_algorithm"""
def GCD(a, b):
	a = 12
	b = 4
	while a!=b:
		if a>b:
			a -= b
		else:
			b -= a
	return a

def str2NumList(strn):
	"""Converts a string to a list of integers based on ASCII values"""
	return [ord(chars) for chars in strn]

def numList2String(l):
	"""Converts a list of integers to a string bsed on ASCII values"""
	return ''.join(map(chr, l))

def encrypt(_g, _s, _e, _n, _m):
	r = randint(3, _m)
	g = gmpy2.mpz(_g)
	s = gmpy2.mpz(_s)
	e = gmpy2.mpz(_e)
	n = gmpy2.mpz(_n)
	m = gmpy2.mpz(_m)
	# return gmpy2.mpz(str(g))**gmpy2.mpz(str(n))
	# return g**(s**(e%n)) * ((r**m)%(m*m))
	return (powmod(2, 1, 1))


