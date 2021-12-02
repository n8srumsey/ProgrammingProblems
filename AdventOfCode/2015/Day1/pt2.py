# Day1 Part 2 
data_path = "./input.txt"

with open(data_path) as f:
    data = f.readlines()[0]

floor = 0

for i in range(len(data)):
    if data[i] == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i + 1)
        exit()