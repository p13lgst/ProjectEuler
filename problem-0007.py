"""
Problem 7 - 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(n):
    if n < 2:
        return False

    sqrt_n = n ** 0.5

    for i in primes:
        if i > sqrt_n:
            break
        if n % i == 0:
            return False
    return True


primes = []
counter = 0
num = 2
while True:
    if is_prime(num):
        primes.append(num)
        counter+=1
        if counter == 10001:
            break
    num += 1

print(num)
