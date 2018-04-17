def main():
	target = 100
	print getDigitSum(getFactorial(target))
	print getFactorial(100)

def getDigitSum(n):
	total = 0
	for i in str(n):
		total+=int(i)
		print i, total
	return total

def getFactorial(n):
	factorial = 1
	for i in range(2,n+1):
		factorial*=i
	return factorial

if __name__ == '__main__':
	main()