from corefunc import *
import algs
from re import findall
from decimal import *


def retBin(num):
	retVal = False

	binary = int("{0:b}".format(num))

	retVal = binary

	assert retVal != False
	return(retVal)

def retStrVal(string):
	retVal = False

	strval = "1"
	for i in string:
		if i == " ":
			x = '00'
		else:
			x = str(retInt(i))
			if len(x) == 1:
				x = x.zfill(2)
		strval += x
	strval = int(strval)

	retVal = strval

	assert retVal != False
	return(retVal)

def encrypt(raw, keyCipher):
	rawVal = retStrVal(raw)
	rawBin = retBin(rawVal)
	ciphVal = rawBin * keyCipher
	ciphList = findall("..", str(ciphVal))

	ciphText = ""
	for i in ciphList:
		x = retChar(int(i))
		ciphText += x
	retVal = ciphText

	assert retVal != False
	return(retVal)

def decrypt(ciphered, keyCipher):
	retVal = False

	ciphVal = ""
	for i in ciphered:
		x = str(retInt(str(i)))
		if len(x) == 1:
			x = x.zfill(2)
		ciphVal += x

	ciphVal = int(ciphVal)
	getcontext().prec = 1000
	binVal = str(Decimal(ciphVal) / Decimal(keyCipher))

	rawVal = str(int(binVal, 2))
	rawVal = rawVal[1:]

	rawList = findall("..", rawVal)

	rawText = ""
	for i in rawList:
		x = int(i)
		y = retChar(x)
		rawText += y
	retVal = rawText

	assert retVal != False
	return(retVal)

def main():
	raw = input("Text to crypt: ")
	key = input("Key to crypt with: ")

	keyCipher = algs.genKeyCipher(key)
	crypted = encrypt(raw, keyCipher)

	uncrypted = decrypt(crypted, keyCipher)

	print(crypted)
	print(uncrypted)





main()
