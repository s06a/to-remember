# Question
"""convert integer to binary"""

# Answer


def binary(n):
    """n is integer
    returns binary number
    """
    output = []

    while n != 0:
        output.append(n % 2)
        n = n // 2
    output = output[::-1]
    output = int(''.join(map(str, output)))

    return output


if __name__ = "__main__":
    n = int(input())
    output = binary(n)
    print(output)
