input_path = "./data.txt"

commands = []

with open(input_path) as f:
    commands = f.readlines()
    commands = [m.rstrip() for m in commands]
    
depth = 0
position = 0
aim = 0

for c in commands:
    if 'forward' in c:
        position += int(''.join(l for l in c if l.isdigit()))
        depth += aim * int(''.join(l for l in c if l.isdigit()))
    elif 'up' in c:
        aim -= int(''.join(l for l in c if l.isdigit()))
    else: # down
        aim += int(''.join(l for l in c if l.isdigit()))

        
print(depth, position, depth * position)