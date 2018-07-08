def get_sum_of_digits(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


if __name__ == '__main__':
    target = 100
    print(get_sum_of_digits(factorial(target)))
