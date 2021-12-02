# Day3 Part 1 

data_path = "./input.txt"

with open(data_path) as f:
    data = f.readline()
    
houses = set()
x = 0
y = 0

for action in data:
    if action == '^':
        houses.add((x, y))
        y += 1
        houses.add((x, y))
    elif action == 'v':
        houses.add((x, y))
        y -= 1
        houses.add((x, y))
    elif action == '<':
        houses.add((x, y))
        x -= 1
        houses.add((x, y))
    else: # >
        houses.add((x, y))
        x += 1
        houses.add((x, y))

print(len(houses))