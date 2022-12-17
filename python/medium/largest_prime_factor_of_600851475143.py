# Question
"""What is the largest prime factor of the number 600851475143?
source: https://projecteuler.net/problem=3
"""

# Answer


def largest_prime_factor(number):
    """n is integer
    returns largest prime factor of n
    source: https://codereview.stackexchange.com/a/276811
    """
    factor = 2
    remnant = number

    while factor**2 <= remnant:
        if remnant % factor == 0:
            remnant //= factor
        else:
            factor += 1

    return remnant


if __name__ == "__main__":
    n = 600851475143
    print(largest_prime_factor(n))
