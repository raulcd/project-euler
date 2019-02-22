# https://projecteuler.net/problem=9
from math import sqrt


def find(number):
    """
    python -m timeit -s 'from euler.problem009 import find' 'find(1000)'
    5 loops, best of 5: 70.5 msec per loop
    """
    for i in range(1, 1000):
        for j in range(1, 1000):
            c = sqrt((i * i) + (j * j))
            if sum((c, j, i)) == number:
                return int(c) * j * i


print(find(1000))
