"""
Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def get_sieve(size):
    sieve = [1 for i in range(size+1)]
    sieve[0:2] = 0, 0

    max_i = size ** 0.5

    for i, v in enumerate(sieve):
        if i >= max_i:
            break
        if v:
            n = 2
            i_n = i**2
            while i_n <= size:
                sieve[i_n] = 0
                n += 1
                i_n = i * n
    return sieve


if __name__ == '__main__':

    num = 600851475143
    floored_sqrt_num = int(num ** 0.5)

    sieve = get_sieve(floored_sqrt_num)

    for i in range(floored_sqrt_num, 1, -1):
        if sieve[i] and num % i == 0:
            print(i)
            break
