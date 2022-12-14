# Question
'''
check if number is strong; sum of the factorials of each digit is equal to the number
'''

# Answer
def factorial(n: int):
    sum = 1
    while n>0:
        sum *= n
        n -= 1
    return sum

def is_strong(n: int):
    list = [int(n) for n in str(n)]
    sum = 0
    while list:
        sum += factorial(list[0])
        list.pop(0)
    return sum == n 

n = int(input())
print(is_strong(n))
