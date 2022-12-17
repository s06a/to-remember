# Question
"""check if the number is palindorme;
it's equal to its reverse
"""

# Answer


def _palindrome_checker(number):
    """number is integer
    checks if number is palindorme
    returns True or False
    """
    """this function uses python, and
    maybe it's not a very nice way
    to solve a mathematical problem
    """
    number = str(number)

    return number == number[::-1]


def palindrome_checker(number):
    """number is integer
    checks if number is palindorme
    returns True or False
    """
    rev = 0
    num = number

    while number > 0:
        rev = 10 * rev + number % 10
        number = number // 10

    return rev == num


if __name__ == "__main__":
    number = int(input())
    print(palindrome_checker(number))
