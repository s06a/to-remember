# Question
"""function to return all the numbers
not divisible by n and m in a given range
"""

# Answer


def func(m, n, lower_range, upper_range):
    """n, m, lower_range, and upper_range are integers
    returns list of numbers not divisible by n and m
    between lower_range and upper_range
    """
    list = []

    for i in range(lower_range, upper_range):
        if (i % m != 0) and (i % n != 0):
            list.append(i)

    return list


if __name__ == "__main__":
    print(*func(2, 3, 10, 105), sep=' ')
