def copyArray(array):
	copy = []
	for value in array:
		copy= appendToNew(copy, value)
	return copy

def appendToNew(array, value):
	bigger = [0]*(len(array) + 1)
	for i in range(len(array)):
		bigger[i] = array[i]

	bigger[len(bigger) - 1] = value
	return bigger

print(copyArray([1,2,3]))

# How long does copying an array take?
# O(N * (1 + 2 + ... + N) = O(N²)