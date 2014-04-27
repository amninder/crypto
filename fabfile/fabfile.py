# coding=utf-8
from random import randint
from fabric.api import *
from fabric.colors import *
from fabric.operations import *
from crypto import miller_rabin
from crypto import RSA
from gmpy2 import *
import gmpy2

a = gmpy2.xmpz(3) # use 4 for good result
b = gmpy2.xmpz(500)

env.digitParameter = a
env.sample_string = " "
# Step 1
env._p 		= 29
env._q 		= 31
env._r 		= 37
env._s 		= 41
env.allNUmbers = []
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
env._c 		= 0

@task
def getRandomNumber():
	""": get random number based upon Miller Rabin Primality test"""

	env._p = RSA.getRandomPrime()
	env._p **= 521
	print(white("%d"%env._p))

@task
def MREA():
	""": Run MREA algorithm"""
	local("fab step1 step2 step3 step4 step5 step6 encrypt decrypt")

@task
def step1():
	"""STEP 1: get p, q, r, s. All are Primes and of same length.
	"""
	print(white("Executing Step 1 of algorithm."))
	env._p = generatePrime()
	env.allNUmbers.append(env._p)
	while bit_length(env._q) != bit_length(env._p) and env._q not in env.allNUmbers:
		env._q = generatePrime()
	env.allNUmbers.append(env._q)

	while bit_length(env._r) != bit_length(env._p) and env._r not in env.allNUmbers:
		env._r = generatePrime()
	env.allNUmbers.append(env._r)

	while bit_length(env._s) != bit_length(env._p) and env._s not in env.allNUmbers:
		env._s = generatePrime()
	env.allNUmbers.append(env._s)
	print("p = %d, Size: %d"%(env._p, bit_length(env._p)))
	print("q = %d, Size: %d"%(env._q, bit_length(env._q)))
	print("r = %d, Size: %d"%(env._r, bit_length(env._r)))
	print("s = %d, Size: %d"%(env._s, bit_length(env._s)))

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
		env._phi 	= num[2]
		env._lambda	= num[3]
		print("n =\t\t%d, Size: %d"%(env._n, bit_length(env._n)))
		print("m =\t\t%d, Size: %d"%(env._m, bit_length(env._m)))
		print("phi =\t\t%d, Size: %d"%(env._phi, bit_length(env._phi)))
		print("lambda =\t%d, Size: %d"%(env._lambda, bit_length(env._lambda)))
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
	# env._e 	= 47
	env._e = generatePrime()
	# env._e = randrange(20, 100)
	x = gcd(env._e, env._phi)
	while x!=1:
		env._e = generatePrime()
		# env._e = randrange(20, 100)
		x = gcd(env._e, env._phi)
		# print("GCD(%d, %d)=%d"%(env._e, env._phi, x))
	print(white("GCD(%d, %d) = %d"%(env._e, env._phi, x)))
	print("e =\t%d, Size: %d"%(env._e, bit_length(env._e)))

@task
def step4():
	"""Step 4: Compute secret exponentd, such that (e x d)mod phi=1 [1<d<phi]"""
	print(white("\nExecuting step 4 of algorithm"))
	# n = randint(1, env._e)
	env._d = divm(1,env._e , env._phi)
	# env._d = RSA.modinv(float(env._e/(1+(n*env._phi))), env._phi)
	print ("d = %d, Size: %d"%(env._d, bit_length(env._d)))
	print ("(%d*%d) mod %d = %d"%(env._e, env._d, env._phi, (env._d*env._e)%env._phi))

@task
def step5():
	"""Step 5: g = m+1"""
	print(white("Executing step 5 of algorithm"))
	env._g = env._m + 1
	print ("g =\t%d, Size: %d"%(env._g, bit_length(env._g)))

@task
def step6():
	"""Step 5: Compute multiplicative inverse: mu = lambda^-1 mod m"""
	print(white("Executing Step 6 of algorithm"))
	env._mu = RSA.modinv(env._lambda, env._m)
	print("mu =\t%d, Size: %d"%(env._mu, bit_length(env._mu)))

@task
def encrypt():
	print(white("Executing: Encrypting string"))
	# env._str2NumList = RSA.str2NumList(env.sample_string)
	# print env._str2NumList
	# for num in env._str2NumList:
	# # for num in env._encrypted:
	# 	env._encrypted.append(RSA.encrypt(env._g, num, env._e, env._n, env._m)) #(s, e, n, m)
	# for num in env._encrypted:
	# 	print num
	cc = 1
	print("Message: %d"%cc)
	env.c = RSA.encrypt(env._g, cc, env._e, env._n, env._m)
	print("Cipher Text: %d"%env.c)


@task
def decrypt():
	# local("fab step1 step2 step3 step4 step5 step6")
	print(white("Executing: Decryption."))
	# for num in env._encrypted:
	# 	env._decrypted.append(RSA.decrypt(num, env._lambda, env._m, env._d, env._mu, env._n))
	# for num in env._str2NumList:
	# 	print RSA.decrypt(num, env._lambda, env._m, env._d, env._mu, env._n)
	# for num in env._decrypted:
	# 	print num
	print("Decrypted Text: %d"%RSA.decrypt(env.c, env._lambda, env._m, env._d, env._mu, env._n))

@task
def rsa():
	""": RSA Algorithm to encrypt and decrypt"""
	env._p = generateLargePrime(env.digitParameter)
	print("p = %d, Size: %d"%(env._p, bit_length(env._p)))

	while bit_length(env._q) != bit_length(env._p):
		env._q = generateLargePrime(env.digitParameter)
	print("q = %d, Size: %d"%(env._q, bit_length(env._q)))

	env._n = mul(env._p, env._q)
	print("n = %d, Size: %d"%(env._n, bit_length(env._n)))

	env._phi = mul(env._p-1, env._q-1)
	print("phi = %d, Size: %d"%(env._phi, bit_length(env._phi)))

	env._e = generateLargePrime(env.digitParameter)
	x = gcd(env._e, env._phi)
	while x!=1:
		env._e = generateLargePrime(env.digitParameter)
		x = gcd(env._e, env._phi)
		# print("GCD(%d, %d)=%d"%(env._e, env._phi, x))
	print("e = %d, Size: %d"%(env._e, bit_length(env._e)))
	print(red("GCD(%d, %d) = %d"%(env._e, env._phi, x)))

	env._d = divm(1,env._e , env._phi)
	print ("d = %d, Size: %d"%(env._d, bit_length(env._d)))
	print ("(d*e) mod phi = %d"%((env._d*env._e)%env._phi))

	print("Message: %d"%133)
	env._c = pow(133, env._e, env._n)
	print(white("Cipher: %d"%env._c))

	m = pow(env._c, env._d, env._n)
	print(white("Decryted Text: %d"%m))

@task
def plotTime():
	from crypto import plots as plots
	plots.plotGraphMiller()

@task
def test():
	env._p = generatePrime()
	env.allNUmbers.append(env._p)
	while bit_length(env._q) != bit_length(env._p) and env._q not in env.allNUmbers:
		env._q = generatePrime()
	env.allNUmbers.append(env._q)
	while bit_length(env._r)!= bit_length(env._p):
		if env._r not in env.allNUmbers:
			print env.allNUmbers
			env._r = generatePrime()
		else:
			pass
	env.allNUmbers.append(env._q)
	print env.allNUmbers

"""
Some python codes
"""
def getDigits(num): 
	i = 0
	while num>0:
		i += 1
		num /= 10
	return i


def generatePrime():
	n = randint(1, 1000)
	while not miller_rabin.millerRabin(n, 2):
		n = randint(1, 1000)
	return n

def generateLargePrime(p):
	n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	while not miller_rabin.millerRabin(n, 2):
		n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	return n
