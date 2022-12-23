# Question
"""get a list of numbers, return the number which 
has the maximum number of prime factors
"""

# Answer


def number_of_prime_factors(n):
    """Returns number of prime factors for a number.

    n is integer
    returns integer
    """
    factor = 2
    num = 0

    while factor <= n:
        if n % factor == 0:
            n //= factor
            num += 1
        else:
            factor += 1

    return num


if __name__ == "__main__":

    list = [40, 54564654, 1321321, 121]

    print(max((n, number_of_prime_factors(n)) for n in list)[0])
