# coding=utf-8
from random import randrange, randint
from fabric.api import *
from fabric.colors import *
from fabric.operations import *
from crypto import mersenne
from crypto import miller_rabin
from crypto import RSA
from datetime import datetime
from gmpy2 import *
import gmpy2
import sys

a = gmpy2.xmpz(1) # use 4 for good result
b = gmpy2.xmpz(500)
env.digitParameter = a
env.sample_string = "t"
# Step 1
env._p 		= 11
env._q 		= 13
env._r 		= 17
env._s 		= 19

# Step 2
env._n 		= 0
env._m 		= 0
env._phi 	= 0
env._lambda = 0

# Step 3
env._e 		= 0

# Step 4
env._d 		= 0

# Step 5
env._g 		= 0

# Step 6
env._mu 	= 0

env._encrypted = []
env._decrypted = []

@task
def getRandomNumber():
	""": get random number based upon Miller Rabin Primality test"""

	env._p = RSA.getRandomPrime()
	env._p **= 521
	print(white("%d"%env._p))


def testForPrimality():
	""": test if the number is prime or not"""

	if miller_rabin_largeN._isPrime(env._p):
		print(green("%d is a prime number"%env._p))
	else:
		print(red("%d is not a prime number"%env._p))

"""
		Step 1: choose four random numbers
"""
@task
def runAlgorithm():
	local("fab step1 step2 step3 step4 step5 step6 encrypt")

@task
def step1():
	"""STEP 1: get p, q, r, s. e and d are being computed in this step
	"""
	print(white("Executing Step 1 of algorithm."))
	i = 0
	env._p = generateLargePrime(env.digitParameter)
	while bit_length(env._q) != bit_length(env._p):
		env._q = generateLargePrime(env.digitParameter)

	while bit_length(env._r) != bit_length(env._p):
		env._r = generateLargePrime(env.digitParameter)

	while bit_length(env._s) != bit_length(env._p):
		env._s = generateLargePrime(env.digitParameter)
	print("p = %d, Size of Digits: %d"%(env._p, bit_length(env._p)))
	print("q = %d, Size of Digits: %d"%(env._q, bit_length(env._q)))
	print("r = %d, Size of Digits: %d"%(env._r, bit_length(env._r)))
	print("s = %d, Size of digits: %d"%(env._s, bit_length(env._s)))

@task	
def step2():
	"""STEP 2: generate another four numbers from numbers generated from Step 1."""
	print(white("Executing step 2 of algorithm"))
	print("Size of p:\t%d"%bit_length(env._p))
	print("Size of q:\t%d"%bit_length(env._q))
	print("Size of r:\t%d"%bit_length(env._r))
	print("Size of s:\t%d"%bit_length(env._s))
	try:
		assert env._p !=0
		assert env._q !=0
		assert env._r !=0
		assert env._s != 0
		num = RSA.step2(env._p, env._q, env._r, env._s)
		env._n 		= num[0]
		env._m 		= num[1]
		env._phi 	= num[2]
		env._lambda	= num[3]
		print("n =\t\t%d, Size of Digits: %d"%(env._n, bit_length(env._n)))
		print("m =\t\t%d, Size of Digits: %d"%(env._m, bit_length(env._m)))
		print("phi =\t\t%d, Size of Digits: %d"%(env._phi, bit_length(env._phi)))
		print("lambda =\t%d, Size of Digits: %d"%(env._lambda, bit_length(env._lambda)))
	except AssertionError, e:
		print(red("Mr. Singh, you did not run Step 1"))
	else:
		pass
	finally:
		pass

@task
def step3():
	"""Step 3: Choose an integer e, such that GCD(e, phi)=1"""
	print(white("\nExecuting step 3 of algorithm"))
	# env._e 	= 23
	env._e = generateLargePrime(env.digitParameter)
	x = gcd(env._e, env._phi)
	while gcd==1:
		env._e = generateLargePrime(env.digitParameter)
		x = gcd(env._e, env._phi)
		print("GCD(%d, %d)=%d"%(env._e, env._phi, x))
	print("GCD(%d, %d) = %d"%(env._e, env._phi, x))
	print("e =\t%d"%(env._e))

@task
def step4():
	"""Step 4: Compute secret exponentd, such that (e x d)mod phi=1 [1<d<phi]"""
	print(white("\nExecuting step 4 of algorithm"))
	n = randint(1, env._e)
	env._d = RSA.modInvEuclid(env._e, env._lambda)
	# env._d = RSA.modinv(float(env._e/(1+(n*env._phi))), env._phi)
	print ("d:\t %d, Size of digits: %d"%(env._d, bit_length(env._d)))
	print ("(d*e) mod phi = %d"%((env._d*env._e)%env._lambda))

@task
def step5():
	"""Step 5: g = m+1"""
	print(white("Executing step 5 of algorithm"))
	env._g = env._m + 1
	print ("g =\t%d, Size of digits: %d"%(env._g, bit_length(env._g)))

@task
def step6():
	"""Step 5: Compute multiplicative inverse: mu = lambda^-1 mod m"""
	print(white("Executing Step 6 of algorithm"))
	env._mu = RSA.modinv(env._lambda, env._m)
	print("mu =\t%d, Size of digits: %d"%(env._mu, bit_length(env._mu)))

@task
def encrypt():
	print(white("Executing: Encrypting string"))
	env._str2NumList = RSA.str2NumList(env.sample_string)
	print env._str2NumList
	for num in env._str2NumList:
		env._encrypted.append(RSA.encrypt(env._g, num, env._e, env._n, env._m)) #(s, e, n, m)
	for num in env._encrypted:
		print num


@task
def decrypt():
	# local("fab step1 step2 step3 step4 step5 step6")
	print(white("Executing: Decryption."))
	for num in env._str2NumList:
		env._decrypted.append(RSA.decrypt(num, env._lambda, env._m, env._d, env._mu, env._n))
	# for num in env._str2NumList:
	# 	print RSA.decrypt(num, env._lambda, env._m, env._d, env._mu, env._n)
	for num in env._decrypted:
		print num

@task
def test():
	pass

def getDigits(num): 
	i = 0
	while num>0:
		i += 1
		num /= 10
	return i

def generateLargePrime(p):
	n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	while not miller_rabin.millerRabin(n, 2):
		n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	return n

