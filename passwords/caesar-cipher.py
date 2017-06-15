#!/usr/bin/python

'''
Caesar Cipher encryption and decryption.
'''

MAX_KEY_SIZE = 26

def getMode():
	while True:
		mode = raw_input("Do you wish to encrypt or decrypt a message?\n").lower()
		if mode in "encrypt e decrypt d".split():
			return mode
		else:
			print "Enter either 'encrypt' or 'e' or 'decrypt' or 'd'."


def getMessage():
	print "Enter your message:"
	return raw_input()


def getKey():
	key = 0
	while True:
		print "Enter the key number (1-{})".format(MAX_KEY_SIZE)
		key = int(raw_input())
		if key >= 1 and key <= MAX_KEY_SIZE:
			return key


def getConvertedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	converted = ""

	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			converted += chr(num)
		else:
			converted += symbol
	return converted

mode = getMode()
message = getMessage()
key = getKey()

print "Your converted text is:"
print getConvertedMessage(mode, message, key)