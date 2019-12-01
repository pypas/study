def product(a,b):
	sum = 0
	for i in range(b):
		sum += a
	return sum

a = 3
b = 4
print(product(a,b))

# The complexity is O(B)