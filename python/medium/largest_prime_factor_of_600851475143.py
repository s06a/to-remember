# Question
"""What is the largest prime factor of
the number 600851475143?"""

# Answer
def is_prime(n):
    """n is integer
    returns True if n is prime
    and False if n is not prime"""

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def largest_prime_factor(n):
    """n is integer
    returns largest prime factor of n"""
    prime_factors = []

    for i in range(2, int(n**0.5) + 1):
        if is_prime(i) and n % i == 0:
            prime_factors.append(i)

    if len(prime_factors):
        return max(prime_factors)
    else:
        return n

if __name__ == "__main__":
    n = 600851475143
    print(largest_prime_factor(n))
