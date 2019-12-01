def mod(a, b):
	if(b <= 0):
		return -1
	div = int(a / b)
	return a - div * b

a = 10
b = 3

print(mod(a,b))

# The complexity is O(1)