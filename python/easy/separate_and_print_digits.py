# Question
'''
read integer from input, separate digits and print each digit in the below format:
    5: 55555
    0: 
    1: 1
    3: 333
'''

# Answer
def func(n):
    for i in n:
        print(f'{i}: {i * int(i)}')

n = int(input())
func(n)
