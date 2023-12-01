import re

digit_words = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def process_line(line):
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

    def convert(s):
        return digit_words.get(s, s)

    return int(convert(digits[0])+(convert(digits[-1])))

# f = open('sample2', 'r')
f = open('data', 'r')
data = [process_line(line.rstrip()) for line in f.readlines()]

print(sum(data))
