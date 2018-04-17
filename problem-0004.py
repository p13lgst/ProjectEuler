"""
Problem 4 -Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest = 0

for i in range(999, 99, -1):
    for j in range(999, i-1, -1):
        num = str(i*j)
        if num == num[::-1]:
            if int(num) > largest:
                largest = int(num)

print(largest)