# -*- coding: utf-8 -*-
import RSA
import miller_rabin
from gmpy2 import *
import gmpy2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from random import randint

param = 1
previous = 0
def plotGraphMiller():
	fig   = plt.figure()
	ax1   = fig.add_subplot(1,1,1)
	plt.suptitle("Bytes VS Time")
	plt.xlabel('Bytes')
	plt.ylabel('NanoSeconds')
	xar   = []
	yar   = []
	def animate(i):
		global param
		global previous
		n = plotMillerTime(param)
		if n[1]>previous:
			previous = n[1]
			xar.append(n[1]/8)
			yar.append(n[0])
			print ("Time: %d"%n[0])
			print ("Bytes: %d"%int(n[1]/8))
			ax1.clear()
			plt.xlabel('Bytes')
			plt.ylabel('NanoSeconds')
			ax1.plot(xar, yar)
		param += 1
	ani = animation.FuncAnimation(fig, animate)
	plt.show()

# ______PLOT FUNCTIONS_______

def plotMillerTime(p):
	multiVar = 1000000000
	mills = int(round(time.time()*multiVar))
	n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	while not miller_rabin.millerRabin(n, 2):
		n = (gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p))+(gmpy2.xmpz(RSA.getRandom())**gmpy2.xmpz(p)-1)
	mills = int(round(time.time()*multiVar)) - mills
	return (mills, bit_length(n), totalDigits(n))

def totalDigits(num): 
	i = 0
	while num>0:
		i += 1
		num /= 10
	return i