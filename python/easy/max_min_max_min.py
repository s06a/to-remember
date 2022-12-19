# Question
"""read a sequence of numbers, if it's length is
even return maximum and delete the element, if it's
length is odd return minimum and delete the element,
do this till the end
"""

# Answer


def return_max_min(sequence):
    """Calculates maximum or minimum of a list.

    sequence is a list of integers
    returns integer

    returns maximum if length of sequence is even
    returns minimum if length of sequence is odd
    """

    if len(sequence) % 2 == 0:
        maximum = max(sequence)
        sequence = sequence.pop(sequence.index(maximum))

        return maximum
    else:
        minimum = min(sequence)
        sequence = sequence.pop(sequence.index(minimum))

        return minimum


if __name__ == "__main__":
    sequence = [int(n) for n in input().split(' ')]

    while sequence:
        print(return_max_min(sequence))
