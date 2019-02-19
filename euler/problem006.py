# https://projecteuler.net/problem=6


def sum_of_squares(number):
    return sum(x * x for x in range(1, number + 1))


def square_of_sum(number):
    return sum(range(1, number + 1)) ** 2


def calculate_square_minus_sum(num):
    """
    python -m timeit -s 'from euler.problem006 import calculate_square_minus_sum' 'calculate_square_minus_sum(100)'
    50000 loops, best of 5: 7.78 usec per loop
    """
    return square_of_sum(num) - sum_of_squares(num)


print(calculate_square_minus_sum(100))
