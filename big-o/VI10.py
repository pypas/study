def sumDigits(n):
	sum = 0
	while(n > 0):
		sum += int(n % 10)
		n /= 10
	return sum

print(sumDigits(1234))

# The complexity is 