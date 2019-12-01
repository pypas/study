def power(a,b):
	if(b < 0):
		return 0
	elif(b==0):
		return 1
	else:
		return a*power(a, b-1)

a = 3
b = 2

print(power(a,b))

# b, b-1, ..., 0

# The complexity is O(B)