"""
Problem 10 - Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sum_of_primes_below(n):
    sieve = [1] * (n + 1)
    sieve[0], sieve[1] = 0, 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            counter = 2
            while i * counter <= n:
                sieve[i * counter] = 0
                counter += 1

    psum = 0
    for i in range(len(sieve)):
        if sieve[i]:
            psum += i
    return psum


target = 2000000
print(sum_of_primes_below(target))
