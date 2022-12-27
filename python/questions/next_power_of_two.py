# Question
"""read a number from input and return
two raised to the next power of two which
is greater than the number
"""

# Answer
import math


def next_power_of_two(n):
    """Calculates the smallest power of two, which is greater than n.

    n is integer
    returns integer
    """
    p = round(math.log(n, 2))

    if 2 ** p != n and 2 ** p > n:
        return 2 ** p
    else:
        return 2 ** (p+1)


if __name__ == "__main__":
    n = int(input())
    next_power_of_two(n)
