# Question
"""Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.
source: https://projecteuler.net/problem=6
"""

# Answer


def square_of_sum(i, j):
    """Calculates square of the sum of numbers in a range.

    i is integer
    j is integer
    returns integer
    """

    return sum(range(i, j + 1)) ** 2


def sum_of_squares(i, j):
    """Calculates sum of the squares of numbers in a range.

    i is integer
    j is integer
    returns integer
    """

    return sum(i**2 for i in range(i, j + 1))


if __name__ == "__main__":
    i, j = 1, 100
    print(square_of_sum(i, j) - sum_of_squares(i, j))
