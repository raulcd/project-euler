# https://projecteuler.net/problem=7
from math import sqrt


def smallest_prime(number):
    # If a number is a factor of two numbers a*b smallest factor has
    # to be maximum the square root (a == b) otherwise one will be smaller
    upper_factor = int(sqrt(number)) + 1
    for possible_prime in range(2, upper_factor):
        if number % possible_prime == 0:
            return possible_prime


def find_primes(elements):
    """
    python -m timeit -s 'from euler.problem007 import find_primes' '[x for x in find_primes(10001)][-1]'
    2 loops, best of 5: 139 msec per loop
    """
    number = 3
    primes = [2]
    while len(primes) < elements:
        yield number
        primes.append(number)
        found_next = False
        while not found_next:
            # We know the number cannot be odd, we start with 3 and
            # add 2 every time to look only even numbers
            number += 2
            if not smallest_prime(number):
                found_next = True


print([x for x in find_primes(10001)][-1])
