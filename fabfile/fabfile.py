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

a = gmpy2.xmpz(1) # use 4 for good result
b = gmpy2.xmpz(500)
env.digitParameter = a
env.sample_string = "This is a sample sentence."
# Step 1
env._p 		= 0
env._q 		= 0
env._r 		= 0
env._s 		= 0

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
def step1():
	"""STEP 1: get p, q, r, s. e and d are being computed in this step
	"""
	print(white("Executing Step 1 of algorithm."))
	i = 0
	env._p = generateLargePrime(env.digitParameter)
	while getDigits(env._q) != getDigits(env._p):
		env._q = generateLargePrime(env.digitParameter)

	while getDigits(env._r) != getDigits(env._p):
		env._r = generateLargePrime(env.digitParameter)

	while getDigits(env._s) != getDigits(env._p):
		env._s = generateLargePrime(env.digitParameter)
	print("p = %d, No. of Digits: %d"%(env._p, getDigits(env._p)))
	print("q = %d, No. of Digits: %d"%(env._q, getDigits(env._q)))
	print("r = %d, No. of Digits: %d"%(env._r, getDigits(env._r)))
	print("s = %d, No. of digits: %d"%(env._s, getDigits(env._s)))
	#print("e = %d, No. of digits: %d"%(env._e, getDigits(env._e)))
	# print("d = %d, No. of digits: %d"%(env._d, getDigits(env._d)))

@task	
def step2():
	"""STEP 2: generate another four numbers from numbers generated from Step 1."""
	print(white("Executing step 2 of algorithm"))
	try:
		assert env._p !=0
		assert env._q !=0
		assert env._r !=0
		assert env._s != 0
		num = RSA.step2(env._p, env._q, env._r, env._s)
		env._n 		= num[0]
		env._m 		= num[1]
		env._phi 	= num[2]#(env._e * env._d) - 1#num[2]
		env._lambda	= num[3]
		print("n =\t\t%d, No. of Digits: %d"%(env._n, getDigits(env._n)))
		print("m =\t\t%d, No. of Digits: %d"%(env._m, getDigits(env._m)))
		print("phi =\t\t%d, No. of Digits: %d"%(env._phi, getDigits(env._phi)))
		print("lambda =\t%d, No. of Digits: %d"%(env._lambda, getDigits(env._lambda)))
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
	env._d = randint(1, env._phi)
	x = f_mod((env._e*env._d), env._phi)
	while x==1:
		env._d = randint(1, env._phi)
		x = f_mod((env._e*env._d), env._phi)
	print("d =\t%d"%(env._d))

@task
def step5():
	"""Step 5: g = m+1"""
	print(white("Executing step 5 of algorithm"))
	env._g = env._m + 1
	print ("g =\t%d, No. of digits: %d"%(env._g, getDigits(env._g)))

@task
def step6():
	"""Step 5: Compute multiplicative inverse: mu = lambda^-1 mod m"""
	print(white("Executing Step 6 of algorithm"))
	env._mu = RSA.modinv(env._lambda, env._m)
	print("mu =\t%d, No. of digits: %d"%(env._mu, getDigits(env._mu)))

@task
def encrypt():
	print(white("Executing: Encrypting string"))
	env._str2NumList = RSA.str2NumList(env.sample_string)
	print(env._str2NumList)
	print(RSA.numList2String(RSA.str2NumList(env.sample_string)))
	# a = env._str2NumList[0]
	# print a
	# RSA.encrypt(env._g, a, env._e, env._n, env._m)
	#print RSA.modularExp(2, 34, pow(10,10))
	for num in env._str2NumList:
		print RSA.encrypt(env._g, num, env._e, env._n, env._m) #(s, e, n, m)

@task
def test():
	p

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

