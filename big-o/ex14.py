def allFib(n):
	for i in range(n):
		print(str(i) + ": " + str(fib(i)))

def fib(n):
	if(n <= 0):
		return 0
	elif(n == 1):
		return 1
	else:
		return fib(n-1) + fib(n-2)

allFib(6)

# fib(1) -> 2, fib(2) -> 2^2 -> fib(3) -> 2^3
# 2 + 2^2 + 2^3 + ... + 2^N = 2(2^N - 1)/(2 - 1)
# The complexity is O(2^(N+1))