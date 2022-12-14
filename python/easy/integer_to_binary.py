# Question
'''
convert integer to binary
'''

# Answer
def binary(n):
    output = []
    while n != 0:
        output.append(n % 2)
        n = n // 2
    output = output[::-1]
    output = int(''.join(map(str, output)))
    return output

n = int(input())
output = binary(n)
print(output)
