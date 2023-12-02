import re


def process_line(line):
    game_ids = re.findall(r'Game.(\d+)', line)
    blues = re.findall(r'(\d+) blue', line)
    reds = re.findall(r'(\d+) red', line)
    greens = re.findall(r'(\d+) green', line)
    game_id = int(game_ids[0])
    bad_reds = [x for x in reds if int(x)>12]
    bad_greens = [x for x in greens if int(x)>13]
    bad_blues = [x for x in blues if int(x)>14]
    if bad_reds or bad_greens or bad_blues:
        return 0
    return game_id


# f = open('sample', 'r')
f = open('data', 'r')
data = [process_line(line.rstrip()) for line in f.readlines()]

print(sum(data))
