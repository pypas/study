def foo(array):
	sum = 0
	product = 1
	for i in range(len(array)):
		sum += array[i]
	for j in range(len(array)):
		product *= array[j]
	print(str(sum) + ", " + str(product))

foo([1,2,3])

# The complexity is O(N²)