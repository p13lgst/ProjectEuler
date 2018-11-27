"""
Problem 16 - Power digit sum

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


def get_sum_of_digits(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total


target = 2**1000
print(get_sum_of_digits(target))
