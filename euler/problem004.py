# https://projecteuler.net/problem=4


def find_max_palindrome(number):
    """
    We could stop earlier or apply clever math but we brute force
    all possible combinations as is quite quick.
    $ python -m timeit -s 'from euler.problem004 import find_max_palindrome' 'find_max_palindrome(999)'
    1 loop, best of 5: 483 msec per loop
    """
    max_result = 0
    for first_number in range(number, 1, -1):
        for second_number in range(number, 1, -1):
            possible_palindrome = first_number * second_number
            if str(possible_palindrome) == str(possible_palindrome)[::-1]:
                if max_result < possible_palindrome:
                    max_result = possible_palindrome
    return max_result


print(find_max_palindrome(999))
