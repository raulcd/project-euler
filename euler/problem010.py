# https://projecteuler.net/problem=10
from math import sqrt


def find_prime_factors(number):
    """
    python -m timeit -s 'from euler.problem010 import find_prime_factors' 'sum(find_prime_factors(2000000))'
    1 loop, best of 5: 928 msec per loop
    """
    count = 2
    non_primes = set()
    all_numbers = set(range(2, number))
    upper_factor = int(sqrt(number)) + 1
    for possible_prime in range(2, upper_factor):
        # Using Erastothenes we calculate the non-primaries until the number.
        # If the number is not in the non-primaries list is a primary as we would
        # have found the primary divisor before
        if possible_prime not in non_primes:
            non_primes.update([x for x in range(count * 2, number + 1, count)])
        count += 1
    # Once we know all non primaries we do a set difference with all of them
    return all_numbers.difference(non_primes)


print(sum(find_prime_factors(2000000)))
