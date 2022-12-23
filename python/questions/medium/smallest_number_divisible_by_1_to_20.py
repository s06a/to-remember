# Question
"""What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
source: https://projecteuler.net/problem=5
"""

# Answer


def divisible_by_range(n, lower_range, upper_range):
    """Checks if a number is divisible by all numbers in a range.

    n is integer
    lower_range is integer
    upper_range is integer
    returns bool
    """
    for i in range(lower_range, upper_range + 1):
        if n % i != 0:
            return False
    return True


if __name__ == "__main__":
    n = 20
    while not divisible_by_range(n, 1, 20):
        n += 10  # it has to be divisible by 5 and 2
    print(n)
