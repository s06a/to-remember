# Question
"""find prime numbers in a range
between lower_range and upper_range
"""

# Answer


def is_prime(n):
    """Checks if n is prime.

    n is integer
    returns True or False
    """

    if n % 2 == 0:
        return False
    temp = 3

    while temp < int(n**0.5) + 1:
        if n % temp == 0:
            return False
        temp += 2

    return True


def prime_numbers(lower_range, upper_range):
    """Lists prime numbers in a range.

    lower_range is integer
    upper_range is integer
    returns list of integers
    """
    list = []

    for n in range(lower_range, upper_range):
        if is_prime(n):
            list.append(n)

    return list


if __name__ == "__main__":
    print(*prime_numbers(10, 100), sep=' ')
