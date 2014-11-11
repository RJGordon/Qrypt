from chardict import *

# General Functionality Not Specific to Any Package #

def retInt(c):
	retVal = False
	if isinstance(c, str):
		retVal = int(chardict[c])

	if c == " ":
		retVal = 0

	return(retVal)

def retChar(n):
	retVal = False
	if isinstance(n, int):
		for key, value in charmap.items():
			if int(value) == n:
				retVal = key
	else:
		print("Invalid type.")

	assert retVal != False
	return(retVal)

def sumStr(s):
	retVal = False
	if isinstance(s, str):
		x = 0
		for i in s:
			y = retInt(i)
			x += y

		retVal = x

	assert retVal != False
	return(retVal)

def meanStr(s):
	retVal = False
	if isinstance(s, str):
		s_len = len(s)
		s_sum = sumStr(s)
		s_mean = s_sum / s_len

		retVal = s_mean

	assert retVal != False
	return(retVal)
