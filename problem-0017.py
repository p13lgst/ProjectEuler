"""
Problem 17 - Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

counted = {
    0: 0,  # don't count
    1: 3,  # one
    2: 3,  # two
    3: 5,  # three
    4: 4,  # four
    5: 4,  # five
    6: 3,  # six
    7: 5,  # seven
    8: 5,  # eight
    9: 4,  # nine
    10: 3,  # ten
    11: 6,  # eleven
    12: 6,  # twelve
    13: 8,  # thirteen
    14: 8,  # fourteen
    15: 7,  # fifteen
    16: 7,  # sixteen
    17: 9,  # seventeen
    18: 8,  # eighteen
    19: 8,  # nineteen
    20: 6,  # twenty
    30: 6,  # thirty
    40: 5,  # forty
    50: 5,  # fifty
    60: 5,  # sixty
    70: 7,  # seventy
    80: 6,  # eighty
    90: 6,  # ninety
    100: 7,  # hundred
    1000: 11  # one thousand
}


def count_letters(n):
    """Count the number of letters in a number"""
    if n == 1000:
        return counted[n]
    if n >= 100:
        if n % 100 == 0:
            return counted[int(n/100)] + counted[100]
        return counted[int(n/100)] + counted[100] + count_letters(n % 100) + 3
    if n >= 10:
        if n <= 20:
            return counted[n]
        return counted[n - n % 10] + counted[n % 10]
    return counted[n]


total = 0
for i in range(1, 1001):
    total += count_letters(i)
print total
