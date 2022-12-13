# Question
'''
Write a function to get a list of numbers. Separate them into odd and even, then return two list, one list of odd numbers and the other list consists of even numbers.
'''

# Answer

def separator(ls):
    list1, list2 = [], []
    for l in ls:
    	if l % 2 == 0:
    		list1.append(l)
    	else:
    		list2.append(l)
    return (list1, list2)
