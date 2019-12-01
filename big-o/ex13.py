def fib(n):
	if(n <= 0):
		return 0
	elif(n == 1):
		return 1
	else:
		return fib(n-1) + fib(n-2)

n = 6
ans = fib(n)
print(ans)

# The complexity is O(2^N)

# There are two branches per call and we go as deep as N => O(branches^depth)