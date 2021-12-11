import sys
sys.path.append('./..')
import utils
import numpy as np
from scipy import signal


def part_1(grid):
    n_flashes = 0
    n_steps = 100
    convolution_filter = np.ones((3, 3))
    convolution_filter[1, 1] = 0

    for _ in range(n_steps):
        # increment each element of the array
        grid = grid + 1

        # generate array of bool, representing where there are flashes
        flashes = grid > 9

        is_flashing = True
        while is_flashing:
            # get an ndarray of ints where for each location there is a flash, 
            # the filter is applied, increasing surrounding tiles by 1
            neighbor_flashes = signal.convolve(flashes, convolution_filter, mode='same')

            # increase the grid by the result of all flashes
            new_grid = grid + neighbor_flashes

            # get grid representing all flashes occurring after this round of flashes
            new_flashes = new_grid > 9

            # get bool representing if there are any positions where there was a flash 
            # that was not in the previous
            is_flashing = (new_flashes & ~flashes).sum().sum() > 0
            flashes = new_flashes
        grid = new_grid
        grid[flashes] = 0
        n_flashes += new_flashes.sum().sum()
    return n_flashes


def part_2(grid):
    n_steps = 100000
    convolution_filter = np.ones((3, 3))
    convolution_filter[1, 1] = 0

    for step in range(n_steps):
        # increment each element of the array
        grid = grid + 1

        # generate array of bool, representing where there are flashes
        flashes = grid > 9

        is_flashing = True
        while is_flashing:
            # get an ndarray of ints where for each location there is a flash, 
            # the filter is applied, increasing surrounding tiles by 1
            neighbor_flashes = signal.convolve(flashes, convolution_filter, mode='same')

            # increase the grid by the result of all flashes
            new_grid = grid + neighbor_flashes

            # get grid representing all flashes occurring after this round of flashes
            new_flashes = new_grid > 9

            # get bool representing if there are any positions where there was a flash 
            # that was not in the previous
            is_flashing = (new_flashes & ~flashes).sum().sum() > 0
            flashes = new_flashes
        grid = new_grid
        grid[flashes] = 0
        if flashes.all().all():
            return step + 1

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.read_nparray_from_digits()
    
    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))