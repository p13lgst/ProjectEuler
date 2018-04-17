"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

Obs.: The 1000-digit number is in the file "8.txt"
"""


def multiply(*args):
    total = 1
    for i in args:
        total *= int(i)
    return total


file = open("8.txt")
number = "".join(i for i in file.read().split())
file.close()

length = 13
greatest = 0
for i in range(1000):
    ajacent_digits = number[i:i+13]
    if "0" in ajacent_digits:
        continue
    product = multiply(ajacent_digits)
    if product > greatest:
        greatest = product

print(greatest)
