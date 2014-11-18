"""
####################################################################

	written for Mersenne twister BY M. Matsumoto and T. Nishimura 
	for the values of MT19937 from table II  of section 8.

###################################################################

AND
  |	0 	1
--|-------
0 |	0 	0
1 |	0 	1

OR
  |	0 	1
--|-------
0 |	0 	1
1 |	1 	1

XOR
  |	0 	1
--|-------
0 |	0 	1
1 |	1 	0


// Create a length 624 array to store the state of the generator
 int[0..623] MT
 int index = 0
 
 // Initialize the generator from a seed
 function initialize_generator(int seed) {
     index := 0
     MT[0] := seed
     for i from 1 to 623 { // loop over each other element
         MT[i] := last 32 bits of(1812433253 * (MT[i-1] xor (right shift by 30 bits(MT[i-1]))) + i) // 0x6c078965
     }
 }
 
 // Extract a tempered pseudorandom number based on the index-th value,
 // calling generate_numbers() every 624 numbers
 function extract_number() {
     if index == 0 {
         generate_numbers()
     }
 
     int y := MT[index]
     y := y xor (right shift by 11 bits(y))
     y := y xor (left shift by 7 bits(y) and (2636928640)) // 0x9d2c5680
     y := y xor (left shift by 15 bits(y) and (4022730752)) // 0xefc60000
     y := y xor (right shift by 18 bits(y))

     index := (index + 1) mod 624
     return y
 }
 
 // Generate an array of 624 untempered numbers
 function generate_numbers() {
     for i from 0 to 623 {
         int y := (MT[i] and 0x80000000)                       // bit 31 (32nd bit) of MT[i]
                        + (MT[(i+1) mod 624] and 0x7fffffff)   // bits 0-30 (first 31 bits) of MT[...]
         MT[i] := MT[(i + 397) mod 624] xor (right shift by 1 bit(y))
         if (y mod 2) != 0 { // y is odd
             MT[i] := MT[i] xor (2567483615) // 0x9908b0df
         }
     }
 }

from:
	Table II: Parameters and k-distribution of Mersenne Twisters for MT19937
"""
_w = 32
_n = 624
_m = 397
_r = 31
_a = 0x9908b0df # a = 2567483615
_u = 11
_s = 7
_b = 0x9d2c5680 # b = 2636928640
_t = 15
_c = 0xefc60000 # c = 4022730752
_l = 18

MT 		= [1 for i in xrange(_n)]
index 	= 0

# last 32 bits
bitmask_upper = (2**_w)-1

# last 31 bit
bitmask_lower = (2**_r)

# to get last 31 bits
get_last_31_bit = (2**_r)-1


def initialize_generator(seed):
	MT[0] = seed
	for i in xrange(1,_n):
		MT[i] = ((1812433253 *MT[i-1])^((MT[i-1]>>30) +1)) & bitmask_upper

def generate_numbers():
	for i in xrange(_n):
		y = (MT[i] & bitmask_lower) + (MT[(i+1) % _n] & get_last_31_bit)
		MT[i] = MT[(i+_m) % _n]^(y>>1)
		if y%2 !=0:
			MT[i] ^= _a

def extract_number():
	global index
	global MT
	if index==0:
		generate_numbers()
	y  = MT[index]
	y ^= y>>_u
	y ^= (y<<_s) & _b 	# 2636928640 is b and 7 is s
	y ^= (y<<_t) & _c 	# 4022730752 is c and 15 is t
	y ^= y >> _l 		# 18 is l

	index = (index+1) % 624 # step 5 of the algorithm
	return y

def retRandom(seed):
	initialize_generator(seed)
	return extract_number()


import miller_rabin
from datetime import datetime
import time



def seed():
    return datetime.now().microsecond
def generateLargePrime(p):
    n = retRandom(p)
    while not miller_rabin.millerRabin(n, 2):
        n = retRandom(p)
    return n

for x in xrange(1,31):
    millis = int(round(time.time() * 1000))
    for x in xrange(1,5001):
        retRandom(seed())# print "%d: %d"%(x, generateLargePrime(seed()))
    millis = int(round(time.time() * 1000))-millis
    with open('file.txt', 'a') as f:
        f.write("%d\n"%(millis))

def rsa():
    for x in xrange(1,31):
        millis = int(round(time.time() * 1000))
        for x in xrange(1,5001):
            _p = retRandom(seed())
        millis = int(round(time.time() * 1000))-millis
        with open('file.txt', 'a') as f:
            f.write("%d\n"%(millis))

