# Question
""" Find the sum of all the multiples of 3 or 5 below 1000
source: https://projecteuler.net/problem=1
"""

# Answer


def find_multiples_in_range_long_version(n, m, lower_range, upper_range):
    """n, m, lower_range, and upper_range are integers
    returns list of multiples of n and m between lower_range
    and upper_range
    """
    list = []

    for i in range(lower_range, upper_range):
        if (i % n == 0) or (i % m == 0):
            list.append(i)

    return list


def find_multiples_in_range(n, m, lower_range, upper_range):
    """n, m, lower_range, and upper_range are integers
    returns list of multiples of n and m between lower_range
    and upper_range
    """

    return [i for i in range(1000) if i % n == 0 or i % m == 0]


if __name__ == "__main__":
    print(sum(find_multiples_in_range(3, 5, 1, 1000)))
