import algs, utils
from re import findall
from decimal import Decimal

def retBin(num):
	retVal = False

	try:
		binary = int("{0:b}".format(num))

		retVal = binary

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)

def retStrVal(string):
	retVal = False

	try:
		strVal = "1" # Initial value of 1 so there is never a leading 0.

		for character in string:
			charVal = str(util.retInt(character))
			if len(charVal) == 1
				charVal = charVal.zfill(2)
			strVal += charVal

		strVal = int(strVal)

		retVal = strVal

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)

def encrypt(raw, keyCipher):
	retVal = False

	try:
		rawVal = retStrVal(raw)
		rawBin = retBin(rawVal)

		ciphVal = rawBin * keyCipher
		ciphList = findall("..", str(ciphVal)) # Breaks up ciphVal into two digit pairs to utilize entire chardict
		ciphText = ""

		for num in ciphList:
			char = util.retChar(int(num))
			ciphText += char

		retVal = ciphText

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)

def decrypt(ciphered, keyCipher):
	retVal = False

	try:
		ciphVal = ""

		for character in ciphered:
			character = str(character)
			charVal = str(util.retInt(character))
			# Keeps charVal two digits
			if len(charVal) == 1:
				charVal = charVal.zfill(2)
			ciphVal += charVal
		ciphVal = int(ciphVal)

		getcontext().prec = 100000
		binVal = str(Decimal(ciphVal) / Decimal(keyCipher))
		rawVal = str(int(binVal, 2))
		rawVal = rawVal[1:] # Removes the initial 1 added in retStrVal
		rawList = findall("..", rawVal) # Breaks rawVal into two digit pairs so it may be properly decrypted.
		rawText = ""

		for num in rawList:
			num = int(num)
			char = util.retChar(num)
			rawText += char

		retVal = rawText

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
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
