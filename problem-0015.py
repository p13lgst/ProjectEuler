from sys import argv

def main():
	n = 20
	print(int(factorial(n*2)/(factorial(n)*factorial(n))))

def factorial(n):
	num = 1
	for i in range(2,n+1):
		num*=i
	return num

if __name__ == '__main__':
	main()
