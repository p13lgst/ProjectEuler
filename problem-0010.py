def getSumOfPrimesBelow(n):
	sieve = getSieve(n)
	sieve[0], sieve[1] = 0, 0
	sieve[1000000] = 0
	for i in range(2,int(n**0.5)):
		if sieve[i]:
			counter = 2
			while i*counter <= n:
				sieve[i*counter] = 0
				counter+=1
	sum = 0
	for i in range(len(sieve)):
		if sieve[i]:
			sum+=i
	return sum



def getSieve(n):
	return [1 for i in range(0, n+1)]
	

def main():
	target = 2000000
	print(getSumOfPrimesBelow(target))

if __name__ == '__main__':
	main()