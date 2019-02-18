# https://projecteuler.net/problem=1


def sum_prob_1_with_mod():
    """
    Using sets and mod
    """
    return sum(
        set([x for x in range(0, 1000) if x % 3 == 0]).union(
            set([x for x in range(0, 1000) if x % 5 == 0])
        )
    )


def sum_prob_1_with_step_in_range():
    """
    Using sets and step in range
    """
    return sum(
        set([x for x in range(0, 1000, 3)]).union(
            set([x for x in range(0, 1000, 5)])
        )
    )


print(sum_prob_1_with_mod())
print(sum_prob_1_with_step_in_range())
