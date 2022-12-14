# Question
'''
check if the number is palindorme; it's equal to its reverse
'''

# Answer
def palindrome_checker(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False

number = int(input())
palindrome_checker(number)
