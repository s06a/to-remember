# Question
"""function to return all the numbers
not divisible by n and m in a given range
"""

# Answer


def not_divisible_by(m, n, lower_range, upper_range):
    """Lists all the numbers not divisible by m and n in a range.

    n is integer
    m is integer
    lower_range is integer
    upper_range is integer
    returns list of integers
    """
    list = []

    for i in range(lower_range, upper_range):
        if (i % m != 0) and (i % n != 0):
            list.append(i)

    return list


if __name__ == "__main__":
    print(*func(2, 3, 10, 105), sep=' ')
