def reverse(array):
	half = len(array) / 2
	for i in range(int(half)):
		other = len(array) - i - 1;
		temp = array[i]
		array[i] = array[other]
		array[other] = temp

array = [1,2,3,4]
reverse(array)
print(array)

# The complexity is N/2 i.e. O(N)