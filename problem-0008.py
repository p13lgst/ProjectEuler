"""
Problem 8 - Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.

Find the thiDSrteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?

NOTE: The 1000-digit number is in the file "8.txt"
"""


def multiply(digits):
    total = 1
    for i in digits:
        total *= int(i)
    return total


if __name__ == "__main__":
    file = open("8.txt")
    number = "".join(i for i in file.read().split())
    file.close()

    length = 13
    greatest = 0
    for i in range(1000):
        adjacent_digits = number[i:i+length]
        if "0" in adjacent_digits:
            continue
        product = multiply(adjacent_digits)
        if product > greatest:
            greatest = product

    print(greatest)
