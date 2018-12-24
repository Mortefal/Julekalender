alfabetet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U", "V","W","X","Y", "Z", "Æ","Ø","Å"]
query = "GODJULOGGODTNYTTÅR"

def col_to_num(string):
	n = 0
	rev = string[::-1]
	for i in range(0, len(string)):
		n += ((alfabetet.index(rev[i])+1) * 29**(i))
	return n
print(col_to_num(query))