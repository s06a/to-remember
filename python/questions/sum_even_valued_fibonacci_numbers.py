# Question
"""By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum
of the even-valued terms
source: https://projecteuler.net/problem=2
"""

# Answer


def is_even(n):
    """Checks if n is even

    n is integer
    returns True or False
    """

    return n % 2 == 0


if __name__ == "__main__":
    i, j = 1, 1
    sum = 0

    while j < 4 * 10**6:
        if is_even(j):
            sum += j
        i, j = j, i + j
    print(sum)
