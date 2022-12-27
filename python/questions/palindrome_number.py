# Question
"""check if the number is palindorme;
it's equal to its reverse
"""

# Answer


def palindrome_checker(number):
    """Checks if a number is palindrome.

    number is integer
    returns True or False
    """

    return str(number) == str(number)[::-1]


def non_pythonic_palindrome_checker(number):
    """Checks if a number is palindorme.

    number is integer
    returns True or False
    """
    rev = 0
    num = number

    while number > 0:
        rev = 10*rev + number % 10
        number //= 10

    return rev == num


if __name__ == "__main__":
    number = int(input())
    print(palindrome_checker(number))
