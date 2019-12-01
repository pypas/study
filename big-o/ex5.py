def printUnorderedPairs(arrayA, arrayB):
	for i in range(len(arrayA)):
		for j in range(len(arrayB)):
			for k in range(len(100000)):
				# O(1), doesn't change with N
				print(str(arrayA[i]) + " , " + str(arrayB[j]))

printUnorderedPairs([5,3,6],[1,4,2])

# The complexity is O(A*B)