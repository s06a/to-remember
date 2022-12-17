# Question
"""find prime numbers in a range
between lower_range and upper_range
"""

# Answer


def is_prime(n):
    """n is integer
    checks if n is prime
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
    """lower_range and upper_range are integers
    returns list of prime numbers
    """
    list = []

    for n in range(lower_range, upper_range):
        if is_prime(n):
            list.append(n)

    return list


if __name__ == "__main__":
    print(*prime_numbers(10, 100), sep=' ')
