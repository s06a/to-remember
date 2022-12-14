# Question
'''
find prime numbers in a range
'''

# Answer
def is_prime(n):
    temp = 2
    while temp < n**0.5 + 1:
        if n % temp == 0:
            return False
        temp += 1
    return True

def prime_numbers(lower_range, upper_range):
    list = []
    for n in range(lower_range, upper_range):
        if is_prime(n):
            list.append(n)
    return list

print(*prime_numbers(10, 100), sep=' ')
