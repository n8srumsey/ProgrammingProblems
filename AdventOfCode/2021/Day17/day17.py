import sys
sys.path.append('./..')
import utils
import math

def process_input(data: str):
    x_range = data[data.find('x=') + 2 : data.find(', y')]
    x_vals = [int(x) for x in x_range.split('..')]
    y_range = data[data.find('y=') + 2 :]
    y_vals = [int(y) for y in y_range.split('..')]
    area = {'x': x_vals, 'y': y_vals}
    return area

def pos_in_target(area, x, y):
    within_x = x >= min(area['x']) and x <= max(area['x'])
    within_y = y >= min(area['y']) and y <= max(area['y'])
    return within_x and within_y

def target_is_left(area):
    return max(0, max(area['x'])) == 0

def target_is_right(area):
    return min(0, min(area['x'])) == 0

def target_is_below(area):
    return max(0, max(area['y'])) == 0

def target_is_above(area):
    return min(0, min(area['y'])) == 0

def past_target_x(area, x):
    if target_is_left(area):
        return x < min(area['x'])
    if target_is_right(area):
        return x > max(area['x'])

def below_target(area, y):
    return y < min(area['y'])

def past_target(area, x, y, vel_x):
    return past_target_x(area, x) or (below_target(area, y) and vel_x == 0)

def step(x, y, vel_x, vel_y):
    if vel_x != 0:
        if x > 0:
            vel_x -=1
        else:
            vel_x += 1
    return x + vel_x, y + vel_y, vel_x, vel_y - 1

def test_velocity(area, vel_x, vel_y):
    max_y = 0
    x = 0
    y = 0
    hits_target = False

    while not past_target(area, x, y, vel_x):
        x, y, vel_x, vel_y = step(x, y, vel_x, vel_y)
        max_y = max(max_y, y)
        if pos_in_target(area, x, y):
            hits_target = True
    return hits_target, max_y

def part_1(data):
    max_y = 0
    for vel_x in range(min(1, min(data['x'])), max(0, max(data['x']))):
        for vel_y in range(max(0, max([abs(y) for y in data['y']]))):
            hits_target, y = test_velocity(data, vel_x, vel_y)
            if hits_target:
                max_y = max(max_y, y)
    return max_y

def part_2(data):
    velocities = set()
    for vel_x in range(min(1, min(data['x'])), max(0, max(data['x']))):
        for vel_y in range(min(0, min(data['y'])), max(0, max([abs(y) for y in data['y']]))):
            hits_target, _ = test_velocity(data, vel_x, vel_y)
            if hits_target:
                velocities.add((vel_x, vel_y))
    return len(velocities)

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.readlines()[0]
    
    data = process_input(data)
    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))