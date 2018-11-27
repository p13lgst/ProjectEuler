"""
Problem 5 - Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b//gcd(a, b)


lcm_1_to_20 = 1
for i in range(2, 21):
    lcm_1_to_20 = lcm(i, lcm_1_to_20)

print(lcm_1_to_20)
