emojis = "😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎"

emojiNumber = []

for i in range(0, len(emojis)):
	x = ord(emojis[i])
	emojiNumber.append(x)

def decryption(number):
	temp = ""
	lowest = 65 # A
	highest = max(number) # Største unicoden.
	difference = highest - lowest 
	for i in range(difference, highest):
		temp = ""
		for elem in number:
			temp += (chr(elem - i + lowest))
	return temp
x = decryption(emojiNumber)
print(x)
