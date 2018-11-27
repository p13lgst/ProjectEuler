"""
Problem 23 - Non-abundant sums
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

# TODO: Find a faster algorithm


def is_abundant(n):
    return sum(i for i in range(1, n) if n % i == 0) > n


abundants = set()
for i in range(12, 28123):
    if is_abundant(i):
        abundants.add(i)

total = 0
for i in range(24, 28123):
    in_result = True
    for j in abundants:
        if i - j in abundants:
            in_result = False
            break
    if in_result:
        total += i

print(total)