# https://projecteuler.net/problem=3

from math import sqrt


def smallest_prime(number):
    # If a number is a factor of two numbers a*b smallest factor has
    # to be maximum the square root (a == b) otherwise one will be smaller
    upper_factor = int(sqrt(number)) + 1
    for possible_prime in range(2, upper_factor):
        if number % possible_prime == 0:
            return possible_prime


def find_prime_factors(number, results=[]):
    """
    Results is created once and we use python reference to reuse the same list.
    $ python -m timeit -s 'from euler.problem003 import find_prime_factors' 'find_prime_factors(600851475143)'
    2000 loops, best of 5: 175 usec per loop
    """
    prime = smallest_prime(number)
    if prime:
        # If we have found a prime it means the number is not prime itself
        # so we keep recursively calling
        results.append(prime)
        number = number // prime
        find_prime_factors(number, results)
    else:
        # We have finished as we haven't found a prime
        # that's the biggest number. Append to the results for completeness
        results.append(number)
    return results


result = find_prime_factors(600851475143)
print(result)
