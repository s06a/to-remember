# Question
'''
read a number from input and return the next power of two which is greater than the number
'''

# Answer
import math

def next_power_of_two():
	p = round(math.log(n, 2))
	if 2**p != n and 2**p > n:
		return 2**p
	else:
		2**(p+1)

n = int(input())
next_power_of_two(n)
