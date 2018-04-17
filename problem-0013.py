def main():
	nums = getNums(open('13.txt').read().split())
	print str(sum(nums))[:10]

def getNums(txt):
	nums = []
	for i in txt:
		nums.append(int(i[:14]))
	return nums

if __name__ == '__main__':
	main()