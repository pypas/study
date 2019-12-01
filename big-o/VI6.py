def sqrt(n):
	guess = 1
	while(guess*guess <=n):
		if(guess * guess == n):
			return guess
		guess += 1
	return -1

print(sqrt(25))

# The complexity is O(sqrt(N))