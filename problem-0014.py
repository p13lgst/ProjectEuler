#############################################################################################
### ProjectEuler.net - Problem 14
###
### The following iterative sequence is defined for the set of positive integers:
###
### n → n/2 (n is even)
### n → 3n + 1 (n is odd)
###
### Using the rule above and starting with 13, we generate the following sequence:
###
### 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
### It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
###
### Which starting number, under one million, produces the longest chain?
###
### NOTE: Once the chain starts the terms are allowed to go above one million.
##################################################################################################


# Store the sequences already found
seqlegths = {}

def main():

	i = 1
	largest = [0, 0]
	for i in range(1000000):
		length = getSequenceLength(i)
		seqlegths[i] = length

		# If the length found is greater than the next, change the largest
		if length > largest[1]:
			largest = [i, length]
	print(largest[0])

# Get the sequence of the lengths
def getSequenceLength(num):
	count = 1 
	while num > 1:

		# Break the loop if get to an sequence already done.
		if num in seqlegths.keys():
			count+=seqlegths[num] - 1
			break
		if num%2 == 0:
			num /= 2
		else:
			num = num*3 + 1
		count+=1
	return count

if __name__ == '__main__':
	main()
