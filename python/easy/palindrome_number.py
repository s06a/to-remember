# Question
'''
check if the number is palindorme; it's equal to its reverse
'''

# Answer
def _palindrome_checker(number):
    '''
    this function uses python, and
    maybe it's not a very nice way
    to solve a mathematical problem
    '''
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False

def palindrome_checker(number):
    rev = 0
    num = number
    while number > 0:
        rev = 10 * rev + number % 10
        number = number // 10
    return rev == num

number = int(input())
print(palindrome_checker(number))
