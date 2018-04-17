letterCountMap = {
	0   :0, #don't count
	1   :3, #one
	2   :3, #two
	3   :5, #three
	4   :4, #four
	5   :4, #five
	6   :3, #six
	7   :5, #seven
	8   :5, #eight
	9   :4, #nine
	10  :3, #ten
	11  :6, #eleven
	12  :6, #twelve
	13  :8, #thirteen
	14  :8, #fourteen 
	15  :7, #fifteen
	16  :7, #sixteen
	17  :9, #seventeen
	18  :8, #eighteen
	19  :8, #nineteen
	20  :6, #twenty
	30  :6, #thirty
	40  :5, #forty
	50  :5, #fifty
	60  :5, #sixty
	70  :7, #seventy
	80  :6, #eighty
	90  :6, #ninety
	100 :7, #hundred
	1000:11 #one thousand
}

def count_letters(n):
	"""Count the number of letters in a number"""
	if n == 1000:
		return letterCountMap[n]
	if n >= 100:
		if n % 100 == 0:
			return letterCountMap[int(n/100)] + letterCountMap[100]
		return letterCountMap[int(n/100)] + letterCountMap[100] + count_letters(n%100) + 3 
	if n >= 10:
		if n <= 20:
			return letterCountMap[n]
		return letterCountMap[n-n%10] + letterCountMap[n%10]
	return letterCountMap[n]
	

if __name__ == '__main__':
	total = 0;
	for i in range(1,1001):
		total+=count_letters(i)
	print total
