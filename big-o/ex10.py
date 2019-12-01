def isPrime(n): 
	x = 2
	while(x*x <= n):
		if(n % x == 0):
			return False
		x += 1
	return True

x = 3
answer = isPrime(x)
print(str(x) + " is Prime")
print(answer)

# The time complexity is O(sqrt(N))