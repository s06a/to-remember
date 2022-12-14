# Question
'''
get an integer and return its factorial
'''

# Answer
def factorial(n):
    sum = 1
    while n>0:
        sum *= n
        n -= 1
    return sum

n = int(input())
factorial(n)
