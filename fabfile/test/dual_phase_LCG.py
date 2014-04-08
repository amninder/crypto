M1 = 2147483647
M2 = 2147483399
A1 = 40015
A2 = 40692
Q1 = ( M1 / A1 )
Q2 = ( M2 / A2 )
R1 = ( M1 % A1 )
R2 = ( M2 % A2 )

seed1 = 1
seed2 = 1

def jsw_rand():
	global seed1
	global seed2

	seed1 = A1 * (seed1 % Q1) - R1 * (seed1 / Q1)
	seed2 = A2 * (seed2 % Q2) - R2 * (seed2 / Q2)
	if seed1<=0:
		seed1 += M1
	if seed2 <= 0:
		seed2 += M2
	result = seed1 - seed2
	return result

for x in xrange(1,10):
	print("%f"%jsw_rand())