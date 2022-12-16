# Question
"""get a two digit number, return the difference 
between the larger digit and the smaller digit"""

# Answer
def calculate_difference(number):
    """number is a two digits integer
    returns the difference between the 
    larger digit and the smaller digit"""
    number = [int(n) for n in number]
    return max(number)-min(number)

if __name__ == "__main__":
    number = input()
    calculate_difference(number)
