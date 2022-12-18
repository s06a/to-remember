# Question
"""read array and k from input,
rotate the array k times and return
the result
"""

# Answer


def rotate_array(array, steps, clockwise=True):
    """array is a list of integers, steps
    is integer, clockwise is True by default
    the function rotates the array k times
    returns the rotated array
    """

    if clockwise:

        while steps > 0:
            array = [array[-1]] + array[:-1]
            steps -= 1
    else:

        while steps > 0:
            array = array[1:] + [array[0]]
            steps -= 1

    return array


if __name__ == "__main__":
    array, steps = [int(n) for n in input().split(' ')], int(input())
    print(rotate_array(array, steps, False))
