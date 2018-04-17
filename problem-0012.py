def main():
	i = 1
	currentTriangle = 1
	while True:
		if countDivisors(currentTriangle) > 500:
			break
		i+=1
		currentTriangle += i		
		
	print currentTriangle

def countDivisors(n):
	factors = primeFactors(n)
	divisors = 1
	for k in factors:
		divisors *= factors[k] + 1
	return divisors

def primeFactors(n):
	current = 2
	factors = {}
	while n > 1:
		if n%current == 0:
			if factors.has_key(current):
				factors[current] += 1
			else:
				factors[current] = 1
			n /= current
		else:
			current+=1
	return factors


if __name__ == '__main__':
	main()