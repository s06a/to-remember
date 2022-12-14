# Question
'''
check if the given number is abundant; sum of its proper divisors is greater than the number
'''

# Answer
import math

def divisors(number):
    '''
    this function returns divisors except
    the number itself
    '''
    divisors = [1]
    n = 2
    while n <= int(math.sqrt(number))+1:
        if number % n == 0:
            divisors.extend([n, number/n])
        n += 1
    return list(set(divisors))

def check_if_abundant(number):
    if number > sum(divisors(number)):
        return False
    else:
        return True

number = int(input())
check_if_abundant(number)
