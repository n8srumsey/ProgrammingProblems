# Day3 Part 2 

data_path = "./input.txt"

with open(data_path) as f:
    data = f.readline()
    
robo = False
houses = set()

x = 0
y = 0

rx = 0
ry = 0

for action in data:
    
    if action == '^':
        if robo:
            houses.add((rx, ry))
            ry += 1
            houses.add((rx, ry))
        else:
            houses.add((x, y))
            y += 1
            houses.add((x, y))
    elif action == 'v':
        if robo:
            houses.add((rx, ry))
            ry -= 1
            houses.add((rx, ry))
        else:
            houses.add((x, y))
            y -= 1
            houses.add((x, y))
    elif action == '<':
        if robo:
            houses.add((rx, ry))
            rx -= 1
            houses.add((rx, ry))
        else:
            houses.add((x, y))
            x -= 1
            houses.add((x, y))
    else: # >
        if robo:
            houses.add((rx, ry))
            rx += 1
            houses.add((rx, ry))
        else:
            houses.add((x, y))
            x += 1
            houses.add((x, y))
    robo = not robo
    
print(len(houses))