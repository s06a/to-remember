# Question
"""get n numbers from input (separated by space) 
and return the maximum"""

# Answer
def find_maximum(numbers):
    """numbers is a space separated sequence
    returns maximum of the sequence"""
	list = [int(num) for num in numbers] 
	return max(list)

if __name__ == "__main__":
    numbers = input().split(' ')
    find_maximum(numbers)

