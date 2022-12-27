# Question
"""read a text file line by line
and return each line
"""

# Answer


def read_line_by_line(file_path):
    """Reads and yields a text file line by line.

    file_path is string
    returns string
    """

    with open(file_path) as file:
        while file:
            yield file.pop()


if __name__ == "__main__":
    print(read_line_by_line(filename.txt))
