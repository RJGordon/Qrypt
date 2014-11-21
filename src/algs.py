from primelist import primeList
from corefunc import *
from decimal import *
import math

def retPrimeFactors(n):
	retVal = False
	factors = []

	# Uses primeList (list of prime numbers up to 1,000,000) to perform trial division
	# Returns list of prime factors
	for p in primeList:
		if p * p > n:
			break
		while n % p == 0:
			factors.append(p)
			n /= p
	if n < 1:
		factors.append(n)
		retVal = factors
	else:
		print("Factorization failed. Maybe input too large?")

	assert retVal != False
	return(retVal)


# Key Cipher Functions #


# Generates a sequence of numbers (one for each character in key) that will be used to create the key cipher.
def genKeySequence(key):
	retVal = False

	k_len = len(key)

	char_seqs = []
	for i in key:

		x = retInt(i)

		n_list = [x]
		for num in range(0, k_len): # Basically does the fibonacci sequence using i as an input, stores the numbers in n_list
			y = x + n_list[len(n_list) - 1]
			n_list.append(y)

		char_seqs.append(int(''.join(str(n) for n in n_list))) # Takes the fib numbers in n_list and joins them into a single string and appends to char_seqs.  Ex; 1,1,2,3,5,8,13,21,34 -> '112358132134'

	retVal = char_seqs

	assert retVal != False
	return(retVal)


# Complex Mathematical Function used by genKeyCipher
def f(x):
	retVal = False

	H = ( 6.58211928 * 15 ) * ( 10 ** 16 )
	C = 299792458

	# Full Equation Single Line
	"""
	f(x) =
			| (  [ x(atan(H))  /  x^4 - 1/12 ] * [ x(C^2) + (e^pi + 1) ]  )   *   (  [ (2 * sqrt(2)) / 9801] * [ ( (4x)! * (1103 + 26390x) ) / ( (x!)^4 * 396^4) ]  ) |
	"""

	# Equation broken into different steps.

	x_1a = x * math.cos(H)
	x_1b = (x **  4) / (-1/12)
	x_1 = x_1a * x_1b


	x_2a = x * (C ** 1/12) + math.pi * x + 1
	x_2F = Decimal(x_1 / x_2a)

	x_3a = (x + C/ math.sqrt(C) / 9831)
	x_3b = (4 * x) * (1103 + (26390 * x)) * (x ** 4) * (396 ** 4) / x
	x_3F = Decimal(x_3a * x_3b)

	x_4 = Decimal(abs(x_3F * x_2F))

	x_4F = '%g'%(x_4 / x_3F)
	
	retVal = int(math.floor(float(x_4F)))

	assert retVal != False
	return(retVal)


def genKeyCipher(key):
	retVal = False

	k_sum = sumStr(key)
	k_mean = meanStr(key)
	k_seqs = genKeySequence(key)

	keyCipher = ""
	for seq in k_seqs:
		keyCipher += str(f(int(seq + k_sum + k_mean)))

	retVal = int(keyCipher)

	assert retVal != False
	return(retVal)
