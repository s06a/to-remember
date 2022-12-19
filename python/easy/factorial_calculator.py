# Question
"""get an integer and return its factorial"""

# Answer


def factorial(n):
    """Calculates factorial of a number.

    n is integer
    returns integer
    """
    sum = 1

    while n > 0:
        sum *= n
        n -= 1

    return sum


if __name__ == "__main__":
    n = int(input())
    factorial(n)
