"""
Problem 48 - Self powers

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

total = 0

for i in range(1, 1001):
    total += int(str(i**i)[-10:])

print(str(total)[-10:])
