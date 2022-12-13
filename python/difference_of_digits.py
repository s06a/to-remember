# Question
'''
get a two digit number, return the difference between the larger digit and the smaller digit
'''

# Answer

def func(number):
	number = [int(n) for n in str(number)]
	return max(number)-min(number)
