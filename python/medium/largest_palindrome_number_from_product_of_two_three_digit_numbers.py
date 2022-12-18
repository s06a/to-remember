# Question
"""Find the largest palindrome made from the product of two 3-digit numbers
source: https://projecteuler.net/problem=4
"""

# Answer


def is_palindrome(n):
    """n is integer
    checks if n is palindrome
    returns True or False
    """

    return str(n) == str(n)[::-1]


def largest_palindrome(n_digit):
    """n_digit is integer, and indicates
    len of divisors
    returns largest palindrome number, which
    is product or n_digit divisors
    """
    list = []
    for i in range(10 ** (n_digit - 1), 10 ** (n_digit)):
        for j in range(10 ** (n_digit - 1), 10 ** (n_digit)):
            if is_palindrome(i*j):
                list.append(i*j)
    return max(list)


if __name__ == "__main__":
    print(largest_palindrome(3))
