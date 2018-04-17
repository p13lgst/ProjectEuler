def getTriplet(targetSum):
	for i in range(1, targetSum):
		for j in range(i, targetSum):
			if getSumOfTriplet(i, j) == targetSum:
				return (i, j)

def getSumOfTriplet(a,b):
	return a + b + (a**2 + b**2)**0.5

def main():
	targetSum = 1000
	a, b = getTriplet(targetSum)
	c = (a**2 + b**2)**0.5
	print int(a*b*c)

if __name__ == '__main__':
	main()
	