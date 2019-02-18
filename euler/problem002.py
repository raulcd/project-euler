# https://projecteuler.net/problem=2


def fibonacci(last_number):
    """
    $ python -m timeit -s 'from euler.problem002 import fibonacci' 'sum([x for x in fibonacci(4000000) if x % 2 == 0])'
    50000 loops, best of 5: 5.05 usec per loop
    """
    first, second = 1, 1
    while second <= last_number:
        yield first + second
        temp = second
        second = first + temp
        first = temp


print(sum([x for x in fibonacci(4000000000) if x % 2 == 0]))
