"""
Problem 21 - Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def d(n):
    return sum(i for i in range(1, n) if n % i == 0)


total = 0

cache = {}
for i in range(10000):
    if i not in cache:
        d_i = d(i)
        d_d_i = d(d_i)
        cache[i] = d_i
        cache[d_i] = d_d_i
        if i != d_i:
            if d_d_i == i:
                total += i + d_i

print(total)