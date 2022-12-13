# Question
'''
get n numbers from input (separated by space) and return the maximum
'''

# Answer
def find_maximum(numbers):
	list = [int(num) for num in numbers] 
	return max(list)

numbers = input().split(' ')
find_maximum(numbers)

