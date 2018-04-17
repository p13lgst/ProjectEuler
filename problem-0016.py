def main():
	target = 2**1000
	print getDigitSum(target)

def getDigitSum(n):
	total = 0
	for i in str(n):
		total+=int(i)
	return total

if __name__ == '__main__':
	main()