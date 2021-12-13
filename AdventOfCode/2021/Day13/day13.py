import sys
sys.path.append('./..')
import utils
import numpy as np

def process_input(data):
    inpt = {'coords': [], 'folds': []}
    
    now_fold = False
    for l in data:
        if l == '':
            now_fold = True
            continue
        if now_fold:
            if 'x' in l:
                fold_axis = 'x'
            if 'y' in l:
                fold_axis = 'y'
            fold_val = int(l.split('=')[1])
            inpt['folds'].append({'axis': fold_axis, 'val': int(fold_val)})
            continue
        coords = l.split(',')
        inpt['coords'].append((int(coords[0]), int(coords[1])))

    return inpt

def fold(points, fold_info):
    new_points = set()
    if fold_info['axis'] == "y":
        for c in points:
            if c[1] < fold_info['val']:
                new_points.add(c)
            elif c[1] > fold_info['val']:
                new_points.add((c[0], 2 * fold_info['val'] - c[1]))

    if fold_info['axis'] == "x":
        for c in points:
            if c[0] < fold_info['val']:
                new_points.add(c)
            elif c[0] > fold_info['val']:
                new_points.add((2 * fold_info['val'] - c[0], c[1]))
    return new_points

def part_1(data):
    points = set()

    first_fold = data['folds'][0]
    for c in data['coords']:
        points.add(c)
    
    points = fold(points, first_fold)
    return len(points)

def part_2(data):
    points = set()

    folds = data['folds']
    for c in data['coords']:
        points.add(c)
    
    for fold_operation in folds:
        points = fold(points, fold_operation)

    # calc max x
    max_x = 0
    for c in points:
        if c[0] > max_x:
            max_x = c[0]

    # calc max y
    max_y = 0
    for c in points:
        if c[1] > max_y:
            max_y = c[1]

    grid = np.zeros((max_x + 1, max_y + 1))

    for c in points:
        grid[c[0], c[1]] = 1.0

    output = "\n"
    for y in range(grid.shape[1]):
        line = "\n"
        for x in range(grid.shape[0]):
            if grid[x, y]:
                line += "X"
            else:
                line += " "
        output += line
    output += "\n"
    return output

if __name__ == '__main__':
    utils.TESTING = False
    np.set_printoptions(threshold=sys.maxsize, linewidth=100000)

    data = utils.readlines()
    data = process_input(data)
 
    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))