# https://projecteuler.net/problem=5
from collections import Counter
from math import sqrt


def find_prime_factors(number, results=[]):
    """
    Results is created once and we use python reference to reuse the same list.
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


def smallest_prime(number):
    # If a number is a factor of two numbers a*b smallest factor has
    # to be maximum the square root (a == b) otherwise one will be smaller
    upper_factor = int(sqrt(number)) + 1
    for possible_prime in range(2, upper_factor):
        if number % possible_prime == 0:
            return possible_prime


def least_common_multiple(max_num):
    """
    python -m timeit -s 'from euler.problem005 import least_common_multiple' 'least_common_multiple(20)'
    5000 loops, best of 5: 39.8 usec per loop
    """
    count = Counter()
    result = 1
    for number in range(2, max_num + 1):
        # Find the factorization on prime numbers for each element
        primes = find_prime_factors(number, [])
        for prime in primes:
            # For lcm we pick the maximum number of appearances of a prime
            # for each one of the numbers (if we have [2,2,2] (8) we pick it over
            # [2,2] (4) as [2,2,2] will be the lcm of 8 and 2.
            if count[prime] < primes.count(prime):
                count[prime] = primes.count(prime)
    for k, v in count.items():
        # We just multiply all the primes the times found
        result *= k ** v
    return result


print(least_common_multiple(2000))
