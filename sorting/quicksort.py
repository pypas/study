### Quicksort
# We pick a random element of the array (the pivot) so that all elements that are
# smaller than it are placed to the left of all elements greater than it.
# By repeatedly partitioning an array (an its sub-arrays) around an element, the 
# array will eventually become sorted.
import math

input = [4,3,9,7,8,1,6,0]
print("The original array is: ")
print(input)

def swap(array, left, right):
	temp = array[right]
	array[right] = array[left]
	array[left] = temp

def partition(array, left, right):
	middle = math.floor((left+right)/2)
	pivot = array[middle]
	while(left <= right):
		while(array[left] < pivot): 
			left += 1 
		while (array[right] > pivot): 
			right -= 1
		
		if(left <= right):
			swap(array, left, right)
			left += 1
			right -= 1
	return left

def quicksort(array, left, right):
	pivotIndex = partition(array, left, right)
	if(left < pivotIndex-1):
		quicksort(array, left, pivotIndex-1)
	if(right > pivotIndex):
		quicksort(array, pivotIndex, right)

quicksort(input, 0,len(input)-1)
print("The sorted array is: ")
print(input)