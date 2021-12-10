# Day9 Part 2 

# Day9 Part 1 

data_input = "./input.txt"

with open(data_input) as f:
    data= [l.rstrip('\n') for l in f.readlines()]

grid = []
for i, r in enumerate(data):
    grid.append([])
    for c in r:
        grid[i].append(int(c))

already_used = []

def basin(r, c):
    # left right up and down
    if (r, c) in already_used or grid[r][c] == 9:
        return 0

    already_used.append((r, c))
    sum = 1

    # up
    if r != 0:
        sum += basin(r - 1, c)
    
    # down
    if r != len(grid) - 1:
        sum += basin(r + 1, c)

    # left
    if c != 0:
        sum += basin(r, c-1)

    # right
    if c != len(grid[0])-1:
        sum += basin(r, c+1)

    return sum



if __name__ == '__main__':
    answer = 0
    basins = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            basins.append(basin(r, c))
    basins = sorted(basins)

    print(basins[-1], basins[-2], basins[-3])
    print("ANSWER: ", basins[-1] * basins[-2] * basins[-3])