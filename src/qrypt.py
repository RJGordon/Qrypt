import algs, util
from re import findall
from decimal import Decimal, getcontext

# Returns binary version of 'num'
def retBin(num):
	retVal = False

	try:
		binary = int("{0:b}".format(num))

		retVal = binary

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)

# Puts the integer values for each character in 'string' (based on chardict)
# into a string and returns it. - i.e. 'abc' -> 0,1,2 -> '012'
def retStrVal(string):
	retVal = False

	try:
		strVal = "1" # Initial value of 1 so there is never a leading 0.

		for character in string:
			charVal = str(util.retInt(character))

			# Adds leading zero if charVal is single digit so all characters can be broken up into two digit pairs.
			if len(charVal) == 1:
				charVal = charVal.zfill(2)
			strVal += charVal

		strVal = int(strVal)

		retVal = strVal

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)

# Encrypts plaintext 'raw' using given keyCipher
def encrypt(raw, keyCipher):
	retVal = False

	try:
		rawVal = retStrVal(raw)
		rawBin = retBin(rawVal)

		ciphVal = rawBin * keyCipher
		ciphList = findall("..", str(ciphVal)) # Breaks up 'ciphVal' into two digit pairs to utilize entire chardict
		ciphText = ""

		# Gets character values for each two digit number in 'ciphList' and adds them to string 'ciphText'
		for num in ciphList:
			char = util.retChar(int(num))
			ciphText += char

		retVal = ciphText

		print("EN CIPHVAL \n{}".format(ciphVal))

	except Exception as e:
		util.error(e)

	util.checkFail(retVal)
	return(retVal)

# Decrypts encrypted text 'ciphered' using given keyCipher
def decrypt(ciphered, keyCipher):
	retVal = False

	try:
		ciphVal = ""

		# Gets integer value of each character in 'ciphered' and adds them to string 'ciphVal'
		for character in ciphered:
			character = str(character)
			charVal = str(util.retInt(character))
			# Adds leading zero if charVal is single digit two maintain two digit pairs
			if len(charVal) == 1:
				charVal = charVal.zfill(2)
			ciphVal += charVal
		ciphVal = int(ciphVal)

		getcontext().prec = 10000000 # Precision of binVal (must be enough to accomodate 100% precision)
		binVal = str(Decimal(ciphVal) / Decimal(keyCipher))
		rawVal = str(int(binVal, 2))
		rawVal = rawVal[1:] # Removes the initial 1 added in retStrVal

		rawList = findall("..", rawVal) # Breaks rawVal into two digit pairs so it may be properly decrypted.
		rawText = ""

		# Gets character value for each two-digit number in 'rawList' and adds it two 'rawText'
		for num in rawList:
			num = int(num)
			char = util.retChar(num)
			rawText += char

		retVal = rawText

		print("DE CIPHVAL \n{}".format(ciphVal))

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
	print("\n-----------\n")
	print(uncrypted)





main()
