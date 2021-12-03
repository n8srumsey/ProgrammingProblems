# Day6 Part 2 

input_path = "./input.txt"

with open(input_path) as f:
    commands = f.readlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

def parse_commands(c: str):
    if 'toggle' in c:
        c = c[7:]
        parsed = c.split()
        xy1 = [int(i) for i in parsed[0].split(',')]
        xy2 = [int(i) for i in parsed[2].split(',')]
        toggle(xy1[0], xy1[1], xy2[0], xy2[1])
    elif 'turn on' in c:
        c = c[8:]
        parsed = c.split()
        xy1 = [int(i) for i in parsed[0].split(',')]
        xy2 = [int(i) for i in parsed[2].split(',')]
        turn_on(xy1[0], xy1[1], xy2[0], xy2[1])
    elif 'turn off' in c:
        c = c[9:]
        parsed = c.split()
        xy1 = [int(i) for i in parsed[0].split(',')]
        xy2 = [int(i) for i in parsed[2].split(',')]
        turn_off(xy1[0], xy1[1], xy2[0], xy2[1])

def turn_on(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] += 1

def turn_off(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = max(0, grid[i][j] - 1)

def toggle(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] += 2

for command in commands:
    parse_commands(command)

count = 0
for i in range(1000):
    for j in range(1000):
        count += grid[i][j]

print(count)