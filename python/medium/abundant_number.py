# Question
"""check if the given number is abundant;
sum of its proper divisors is greater than the number"""

# Answer
def divisors(number):
    """number is integer
    returns divisors except
    the number itself
    """
    divisors = [1]
    n = 2

    while n <= int(round(number**0.5))+1:
        if number % n == 0:
            divisors.extend([n, number/n])
        n += 1

    return list(set(divisors))

def check_if_abundant(number):
    """number is integer
    checks if number is abundant
    returns True or False"""

    return number > sum(divisors(number))

if __name__ == "__main__":
    number = int(input())
    check_if_abundant(number)
