# Question
"""check if the given number is abundant; sum of
its proper divisors is greater than the number
"""

# Answer


def divisors(number):
    """Lists divisors of number except the number.

    number is integer
    returns list of integers.
    """
    divisors = [1]
    n = 2
    while n <= int(round(number ** 0.5)) + 1:
        if number % n == 0:
            divisors.extend([n, number / n])
        n += 1

    return list(set(divisors))


def check_if_abundant(number):
    """Checks if number is abundant.

    number is integer
    returns True or False.
    """

    return number > sum(divisors(number))


if __name__ == "__main__":
    number = int(input())
    check_if_abundant(number)
