#	Factoring Module for Qrypt	#
#	github.com/RJGordon/Qrypt


def g(x, n):

	retVal = (x ** 2) + 1 % n

	return(retVal)

def gcd(num_a, num_b):

	while num_a != num_b:

		if num_a > num_b:
			num_a -= num_b
		else:
			num_b -= num_a

	return(num_a)


def factorPrimes(num):

	retVal = None
	x, y, d = 2, 2, 1

	x = g(x, num)

	for i in range(0, 2):
		y = g(y, num)

	d = gcd(abs(x - y), num)

	if d != n:
		retVal = d
	else:
		retVal = False
		print("Factorization Failed.")

	return(retVal)
