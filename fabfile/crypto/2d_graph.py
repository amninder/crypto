import time
import RSA
from gmpy2 import *
import matplotlib.pyplot as plt

def generate2d():
	_x = []
	_y = []
	for x in xrange(1,10):
		mil = int(round(time.time())*1000000)
		n = RSA.generateLargePrime(x)
		mil = int(round(time.time())*10000000000) - mil
		_y.append(int(mil))
		_x.append(bit_length(n))
	print _x
	print _y
	# generateGraph(_x, _y)

def generateGraph(_time, _byte):
	plt.plot(_time, _byte, '-')
	# plt.axis([0, 6, 0, 20])
	plt.show()

generate2d()