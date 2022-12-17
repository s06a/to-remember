# Question
"""What is the largest prime factor of the number 600851475143?
source: https://projecteuler.net/problem=3
"""
"""not the fastest algorithm, however, for this question it's
still pretty fast
"""

# Answer


def is_prime(n):
    """n is integer
    returns True if n is prime
    and False if n is not prime
    """

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0:
            return False

    return True


def largest_prime_factor(n):
    """n is integer
    returns largest prime factor of n
    """
    prime_factors = []
    step = 1

    for i in range(2, int(n**0.5) + 1, step):
        if is_prime(i) and n % i == 0:
            prime_factors.append(i)

        if i == 2:
            step += 1

        if i == 5:
            step += 4

    if len(prime_factors):
        return max(prime_factors)
    else:
        return n


if __name__ == "__main__":
    n = 600851475143
    print(largest_prime_factor(n))
