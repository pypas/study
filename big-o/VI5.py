def sqrt(n):
	return sqrt_helper(n,1,n)

def sqrt_helper(n,min,max):
	if(max < min):
		return -1 # No square root

	guess = int((min + max) / 2)
	if (guess * guess == n):
		return guess
	elif (guess * guess < n):
		return sqrt_helper(n, guess+1, max)
	else:
		return sqrt_helper(n,min,guess-1)


print(sqrt(225))

# The complexity is O(log N)
# Basically a binary search 