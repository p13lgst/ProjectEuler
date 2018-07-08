"""
Problem 13 - Large sum

Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.

NOTE: The numbers are in the file '13.txt'
"""


def parse_numbers(txt):
    nums = []
    for i in txt:
        nums.append(int(i[:10]))
        print(i[12], end=" ")
    return nums


if __name__ == '__main__':
    nums = parse_numbers(open('13.txt').read().split())
    print(str(sum(nums))[:10])
