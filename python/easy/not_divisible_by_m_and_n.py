# Question
'''
a function to return all the numbers not divisible by n and m in a given range
'''

# Answer
def func(m, n, lower_range, upper_range):
    list = []
    for i in range(lower_range, upper_range):
        if (i%m != 0) and (i%n != 0):
            list.append(i)
    return list

print(*func(2, 3, 10, 105), sep=' ')
