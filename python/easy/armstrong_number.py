# Question
"""check if a number is an armstring number; sum of all 
digits each raised to the power of the length of the 
number is equal to the number"""

# Answer
def is_armstrong(n: int):
    """n is integer
    returns True or False"""
    list = [n for n in str(n)]
    p = len(list)
    sum = 0
    for i in list:
        sum += int(i)**p
    return sum == n

if __name__ == "__main__":
    n = int(input())   
    print(is_armstrong(n))
