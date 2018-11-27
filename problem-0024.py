"""
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from math import factorial

digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

n = ""
index = 0

target = 10**6

while len(digits):
    for i, d in enumerate(digits, 1):
        digits_left_factorial = factorial(len(digits) - 1)
        if i * digits_left_factorial + index >= target:
            n += str(d)
            index += (i - 1) * digits_left_factorial
            digits.remove(d)
            break
print(n)
