# Question
"""Write a function to get a list of numbers
Separate them into odd and even, then return
two lists, one list of odd numbers and the
other list consists of even numbers"""

# Answer


def separator(ls):
    """ls is a list of integers
    returns even numbers in list1
    and odd numbers in list2"""
    list1, list2 = [], []

    for l in ls:
        if l % 2 == 0:
            list1.append(l)
        else:
            list2.append(l)

    return (list1, list2)


if __name__ == "__main__":
    list = [4, 2, 3, 5, 151511, 12]
    print(separator(list))
