cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
oneKey = input("Write the key: ").upper()

def encryptDecrypt(mode, message, key):
	key *= len(message) // len(key) + 1  
	finalMessage = ""
	for i, j in enumerate(message):
		if mode in ['E','e']:
			temp = ord(j) + ord(key[i])
		else:
			temp = ord(j) - ord(key[i])
		finalMessage += chr(temp % 26 + ord('A'))
	return finalMessage
print("Final message:",encryptDecrypt(cryptMode, startMessage, oneKey))