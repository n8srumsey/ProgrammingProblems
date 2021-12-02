# Day1 Part 1 

data_path = "./input.txt"

with open(data_path) as f:
    data = f.readlines()[0]

floor = 0

for c in data:
    if c == '(':
        floor += 1
    else:
        floor -= 1
        
print(floor)