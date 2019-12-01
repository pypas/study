def printPairs(array):
	for i in range(len(array)):
		for j in range(len(array)):
			print(str(array[i]) + ", " + str(array[j]))

printPairs([1,2,3])

# The complexity is O(N)