def permutation2(str, prefix):
	if(len(str) == 0):
		print(prefix) # O(N)
	else:
		for i in range(len(str)):
			rem = str[0:i] + str[i+1:]
			permutation2(rem, prefix + str[i])

def permutation(str):
	permutation2(str, "")

permutation("tes")

# The complexity is O(N² * N!)

