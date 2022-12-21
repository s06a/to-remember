# Question
""" Find the sum of all the multiples of 3 or 5 below 1000
source: https://projecteuler.net/problem=1
"""

# Answer


def find_multiples_in_range_long_version(n, m, lower_range, upper_range):
    """Finds multiple of n and m in a range.

    n is integer
    m is integer 
    lower_range is integer
    upper_range is integer
    returns list of integers
    """
    list = []

    for i in range(lower_range, upper_range):
        if (i % n == 0) or (i % m == 0):
            list.append(i)

    return list


def find_multiples_in_range(n, m, lower_range, upper_range):
    """Finds multiple of n and m in a range.

    n is integer
    m is integer 
    lower_range is integer
    upper_range is integer
    returns list of integers
    """

    return [i for i in range(lower_range, upper_ranger) if i % n == 0 or i % m == 0]


if __name__ == "__main__":
    print(sum(find_multiples_in_range(3, 5, 1, 1000)))
