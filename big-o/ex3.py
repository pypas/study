def printUnorderedPairs(array):
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			print(str(array[i]) + " , " + str(array[j]))

printUnorderedPairs([1,2,3])

# The complexity is N*N/2, i.e, O(N²)