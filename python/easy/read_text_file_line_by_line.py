# Question
"""read a text file line by line
and return each line
"""

# Answer


def read_line_by_line(file_path):
    """file_path is path to the text file
    reads the file line by line
    returns each line of the file
    """
    with open(file_path) as file:
        while file:
            yield file.pop()


if __name__ == "__main__":
    print(read_line_by_line(filename.txt))
