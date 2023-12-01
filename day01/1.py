import re


def process_line(line):
    digits = re.findall(r'\d', line)
    return int(digits[0]+digits[-1])


# f = open('sample', 'r')
f = open('data', 'r')
data = [process_line(line.rstrip()) for line in f.readlines()]

print(sum(data))
