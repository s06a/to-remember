# Question
"""print hallow square with star
characters"""

# Answer
def hallow_square(n):
    """n is integer
    prints a hallow square with
    star character"""
	for i in range(1, n + 1):
		if i == 1 or i == n:
			print('* '*(n-1) + '*')
		else:
			print('*' + ' '*(2*(n - 1) - 1) + '*')

if __name__ == "__main__":
    n = int(input())
    hallow_square(n)

