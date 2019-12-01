def div(a, b):
	count = 0
	sum = b
	while(sum <= a):
		sum += b
		count += 1
	return count

a = 5
b = 2

print(div(a,b))

# The complexity is O(A/B)