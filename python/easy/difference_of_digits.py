# Question
'''
get a two digit number, return the difference between the larger digit and the smaller digit
'''

# Answer
def calculate_difference(number):
    number = [int(n) for n in number]
    return max(number)-min(number)

number = input()
calculate_difference(number)
