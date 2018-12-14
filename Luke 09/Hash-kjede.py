import urllib.request
import json
import hashlib
response = urllib.request.urlopen('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-hashchain.json')
data = json.load(response)
hashes = []
for elem in data:
	hashes.append(elem)



def computeMd5(letter):
	m = hashlib.md5()
	m.update(letter.encode('utf'))
	return m.hexdigest()

def hashKeyWord():
	return computeMd5("julekalender")

def decryptMessage(hashes, initialHash, message):
	if len(message) == len(hashes):
		return message
	
	for elem in hashes:
		if computeMd5(initialHash + elem["ch"]) == elem["hash"]:
			message += elem["ch"]
			initialHash = computeMd5(initialHash + elem["ch"])

			return decryptMessage(hashes, initialHash, message)
	return message

def main():
	message = decryptMessage(hashes, hashKeyWord(), "")
	print(message)

main()

