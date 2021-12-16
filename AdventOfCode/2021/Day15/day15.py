import sys
sys.path.append('./..')
import utils


def is_in_bounds(position, grid):
	return position[0] in range(len(grid)) and position[1] in range(len(grid[0]))

def part_1(data):
    queue = [(0, 0, 0)]
    costs = {}
    while True:
        cost, x, y = queue[0]
        if x == len(data) - 1 and y == len(data[0]) -1: 
            return cost

        queue = queue[1:]

        adjacent = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        for x_adj, y_adj in adjacent:
            if is_in_bounds((x_adj, y_adj), data):
                new_cost = cost + data[x_adj][y_adj]
                if (x_adj, y_adj) in costs and costs[(x_adj, y_adj)] <= new_cost:
                    continue
                costs[(x_adj, y_adj)] = new_cost
                queue.append((new_cost, x_adj, y_adj))
        queue = sorted(queue)

def part_2(data):
    expanded = [[0 for c in range(5*len(data[0]))] for r in range(5*len(data))]

    for r in range(len(expanded)):
        for c in range(len(expanded[0])):
            dist = r // len(data) + c // len(data[0])
            newval = data[r % len(data)][c % len(data[0])]
            for _ in range(dist):
                newval+=1
                if newval==10:
                    newval=1
            expanded[r][c] = newval
    data = expanded

    queue = [(0, 0, 0)]
    costs = {}
    while True:
        cost, x, y = queue[0]
        if x == len(data) - 1 and y == len(data[0]) -1: 
            return cost

        queue = queue[1:]

        adjacent = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        for x_adj, y_adj in adjacent:
            if is_in_bounds((x_adj, y_adj), data):
                new_cost = cost + data[x_adj][y_adj]
                if (x_adj, y_adj) in costs and costs[(x_adj, y_adj)] <= new_cost:
                    continue
                costs[(x_adj, y_adj)] = new_cost
                queue.append((new_cost, x_adj, y_adj))
        queue = sorted(queue)

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.read_grid_2darray()
    
    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))