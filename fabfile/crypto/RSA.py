import miller_rabin
import mersenne
import math
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