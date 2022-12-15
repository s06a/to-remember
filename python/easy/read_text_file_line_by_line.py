# Question
'''
read a text file line by line
'''

# Answer
def read_line_by_line(file_path):
    with open(file_path) as file:
        for line in file:
            return line
