import urllib.request

response = urllib.request.urlopen('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-vekksort.txt')
numbers = []
for line in response:
	numbers.append(int(line))

def lis(arr): 
	n = len(arr) 

# Declare the list (array) for LIS and initialize LIS 
# values for all indexes 
	lis = [1]*n 

# Compute optimized LIS values in bottom up manner 
	for i in range (1 , n): 
		for j in range(0 , i): 
			if arr[i] >= arr[j] and lis[i] < lis[j] + 1 : 
				lis[i] = lis[j]+1

# Initialize maximum to 0 to get the maximum of all 
# LIS 
	maximum = 0

# Pick maximum of all LIS values 
	for i in range(n): 
		maximum = max(maximum , lis[i]) 
	print(lis)
	return maximum 
# end of lis function 
x = numbers
y=[x[i]+i/len(x) for i in range(len(x))]
print(len(y))
#print(lis([1, 1, 2, 3, 4, 5, 7, 6, 6, 7, 8]))