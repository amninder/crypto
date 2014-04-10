import miller_rabin
import mersenne
from random import randint
import gmpy2
from gmpy2 import *
from datetime import datetime
import math

		
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
	_n 		= mul(p,q)
	_m 		= mul(r,s)
	_phi 	= mul((p-1),(q-1))
	_lambda	= mul((r-1),(s-1))
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

def generateLargePrime(p):
	n = (gmpy2.xmpz(getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(getRandom())**gmpy2.xmpz(p)-1)
	while not miller_rabin.millerRabin(n, 2):
		n = (gmpy2.xmpz(getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(getRandom())**gmpy2.xmpz(p)-1)
	return n

def encrypt(_g, _s, _e, _n, _m):
	r = gmpy2.mpz(randint(3, _m-1))
	g = gmpy2.mpz(_g)
	s = gmpy2.mpz(_s)
	e = gmpy2.mpz(_e)
	n = gmpy2.mpz(_n)
	m = gmpy2.mpz(_m)

	s_e_mod_n 	= pow(s, e, n) 
	r_m = pow(r, m, m*m)
	# e_mod_n = gmpy2.mpz(f_mod(e, n))
	# m_e_mod_n = m**e_mod_n
	# return m_e_mod_n
	return s_e_mod_n * r_m

def decrypt(_c, _lambda, _m, _d, _mu, _n):
	c = gmpy2.mpz(_c)
	lmda = gmpy2.mpz(_lambda)
	m = gmpy2.mpz(_m)
	d = gmpy2.mpz(_d)
	mu = gmpy2.mpz(_mu)
	n = gmpy2.mpz(_n)
	
	c_lambda_m = pow(c, lmda, m**2-1)
	# c_lambda_m -= 1
	c_lambda_m /= m
	c_lambda_m *= f_mod(mu, m)
	c_lambda_m = pow(c_lambda_m, d, n)
	return c_lambda_m

"""http://www.wojtekrj.net/2008/09/pythonalgorithms-fast-modular-exponentiation-script/"""
def modularExp(a, n, m):
	bits = []
	while n:
		bits.append(n%2)
		n /= 2
	solution = 1
	bits.reverse()
	for x in bits:
		solution = (solution*solution) % m
		if x:
			solution = (solution*a) % m
	return solution

def expo(u, m):
	q = m
	prod = 1
	current = u
	while q>0:
		if (q%2)==1:
			prod = current * prod
			q -= 1
			print prod
	current = current * current
	q = q/2
	return prod
