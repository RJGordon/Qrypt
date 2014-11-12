import util, math
from decimal import Decimal


"""
Not Implemented Yet

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
"""

# Key Cipher Functions #


# Generates a sequence of numbers (one for each character in key) that will be used to create the key cipher.
def genKeySequence(key):
	retVal = False

	try:
		k_len = len(key)
		sequences = []

		for character in key:
			x = util.retInt(character)
			num_list = [x]

			# Basically does the fibonacci sequence using i as an input, stores the numbers in n_list
			for num in range(0, k_len):
				fibnum = x + num_list[len(num_list) - 1]
				num_list.append(fibnum)

			# Takes the fib numbers in num_list and joins them into a single string and appends to char_seqs.
																# Ex; 1,1,2,3,5,8,13,21,34 -> '112358132134'
			sequences.append( int( ''.join( str(fibnum) for fibnum in num_list ) ) )

		retVal = sequences

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)


# Complex Mathematical Function used by genKeyCipher
def f(x):
	retVal = False

	try:
		H = ( 6.58211928 * 15 ) * ( 10 ** 16 )
		C = 299792458

		x_1a = x * math.cos(H)
		x_1b = (x **  4) / (-1/12)
		x_1F = x_1a * x_1b

		x_2a = x * (C ** 1/12) + math.pi * x + 1
		x_2F = Decimal(x_1F / x_2a)

		x_3a = (x + C/ math.sqrt(C) / 9831)
		x_3b = (4 * x) * (1103 + (26390 * x)) * (x ** 4) * (396 ** 4) / x
		x_3F = Decimal(x_3a * x_3b)

		x_4 = Decimal(abs(x_3F * x_2F))
		x_4F = float('%g'%(x_4 / x_3F))

		retVal = int(math.floor(x_4F))

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)


def genKeyCipher(key):
	retVal = False

	try:
		k_sum = util.sumStr(key)
		k_mean = util.meanStr(key)
		k_seqs = genKeySequence(key)

		keyCipher = ""
		for seq in k_seqs:
			keyCipher += str(f(int(seq + k_sum + k_mean)))

		retVal = int(keyCipher)

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)
