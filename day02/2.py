import re


def process_line(line):
    game_ids = re.findall(r'Game.(\d+)', line)
    blues = re.findall(r'(\d+) blue', line)
    reds = re.findall(r'(\d+) red', line)
    greens = re.findall(r'(\d+) green', line)
    game_id = int(game_ids[0])
    max_reds = max([int(x) for x in reds])
    max_greens = max([int(x) for x in greens])
    max_blues = max([int(x) for x in blues])
    return max_reds * max_greens * max_blues


# f = open('sample', 'r')
f = open('data', 'r')
data = [process_line(line.rstrip()) for line in f.readlines()]

print(sum(data))
