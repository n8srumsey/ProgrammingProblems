# Day9 Part 1 

data_input = "./input.txt"

with open(data_input) as f:
    data= [l.rstrip('\n') for l in f.readlines()]

grid = []
for i, r in enumerate(data):
    grid.append([])
    for c in r:
        grid[i].append(int(c))

def is_low(r, c):
    height = grid[r][c]
    if r == 0:
        if grid[r+1][c] <= height:
            return False
    elif len(grid) - 1 == r:
        if grid[r-1][c] <= height:
            return False
    else: 
        if grid[r-1][c] <= height or grid[r+1][c] <= height:
            return False
    
    if c == 0:
        if grid[r][c+1] <= height:
            return False
    elif c == len(grid[0])-1:
        if grid[r][c-1] <= height:
            return False
    else: 
        if grid[r][c-1] <= height or grid[r][c+1] <= height:
            return False
    return True

def get_risk(height):
    return 1 + height

if __name__ == '__main__':
    answer = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_low(r,c):
                answer += get_risk(grid[r][c])

    print(answer)