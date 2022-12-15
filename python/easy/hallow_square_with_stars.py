# Question
'''
print hallow square with start character
'''

# Answer
def hallow_square(n):
	for i in range(1, n + 1):
		if i == 1 or i == n:
			print('* '*(n-1) + '*')
		else:
			print('*' + ' '*(2*(n - 1) - 1) + '*')

n = int(input())
hallow_square(n)

