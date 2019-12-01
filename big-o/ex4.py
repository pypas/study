def printUnorderedPairs(arrayA, arrayB):
	for i in range(len(arrayA)):
		for j in range(len(arrayB)):
			if(arrayA[i] < arrayB[j]):
				#O(1)
				print(str(arrayA[i]) + " , " + str(arrayB[j]))

printUnorderedPairs([5,3,6],[1,4,2])

# The complexity is O(A*B)