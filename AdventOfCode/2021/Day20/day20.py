import sys

sys.path.append('./..')
import utils
import numpy as np
from scipy.ndimage import convolve

def process_input(data):
    inpt = {}
    inpt['algo'] = np.array([int(c=='#') for c in data[0]])
    inpt['img'] = np.pad([[int(c=="#") for c in r] for r in data[2:]], (51,51))
    return inpt


def binary_to_decimal():
    return 2 ** np.arange(9).reshape(3,3)


def enhance(img, algo, n):
    if n == 0:
        return img
    img = algo[convolve(img, binary_to_decimal())]
    return enhance(img, algo, n - 1)


def part_1(data):
    img = data['img']
    algo = data['algo']
    return enhance(img, algo, 2).sum()


def part_2(data):
    img = data['img']
    algo = data['algo']
    return enhance(img, algo, 50).sum()

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.readlines()
    data = process_input(data)
    
    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))