"""
Problem 9 - Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def get_triplet(target_sum):
    for i in range(1, target_sum):
        for j in range(i, target_sum):
            if get_sum_of_triplet(i, j) == target_sum:
                return i, j


def get_sum_of_triplet(a, b):
    return a + b + (a**2 + b**2)**0.5


def main():
    target_sum = 1000
    a, b = get_triplet(target_sum)
    c = int((a**2 + b**2)**0.5)
    print(a*b*c)


if __name__ == '__main__':
    main()
