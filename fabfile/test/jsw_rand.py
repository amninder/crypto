M = 2147483647
A = 16807
Q = (M/A)
R = (M % A)


seed = 1

def jsw_rand():
	global seed
	seed = A * (seed % Q) - R * (seed/Q)
	if seed <= 0:
		seed += M
	return seed

def uniform_deviate():
	return float(seed * (1.0/M))


for x in xrange(1,10):
	jsw_rand()
	print("%f" % uniform_deviate())