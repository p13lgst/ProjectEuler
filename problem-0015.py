"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


def factorial(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num


if __name__ == '__main__':
    n = 20
    print(int(factorial(n*2)/(factorial(n)*factorial(n))))
