import sys
sys.path.append('./..')
import utils
import math
import math
from functools import reduce
from itertools import permutations

def process_input(data):
    return list(map(eval, data))

def add_left(e, n):
    """ Adds to left side of a pair """
    # e: input element
    # n: number to add
    # returns: 

    if n is None:
        return e

    # if it is an int, add the desired amount to it
    if isinstance(e, int):
        return e + n

    return [add_left(e[0], n), e[1]]


def add_right(e, n):
    """ Adds to right side of a pair"""
    # e: input element
    # n: number to add
    # returns: 

    if n is None:
        return e

    # if it is an int, add the desired amount to it
    if isinstance(e, int):
        return e + n

    return [e[0], add_right(e[1], n)]


def explode(e, l=4):
    """ Parameters:  """
    # e: the input element
    # l: layers away from reaching the fourth nested list

    """ Return values: bool, any, any, any """
    # Bool: represents if it exploded at all
    # Any: left value to be added to the left
    # Any: The element to replace the current 
    #      element with (if it explodes... 
    #      eventually 0 but if it does not, 
    #      the current real element value)
    # Any: right value to be added to the right

    # other base case
    if isinstance(e, int):
        return False, None, e, None
    
    # base case
    if l == 0:
        return True, e[0], 0, e[1]
    
    # unpack the input list (previous base cases determined if it was a list or not)
    a, b = e

    # explode the left half, if possible
    exp, u, a, v = explode(a, l - 1)
    if exp:
        return True, u, [a, add_left(b, v)], None

    # explode the right half, if possible
    exp, u, b, v = explode(b, l - 1)
    if exp:
        return True, None, [add_right(a, u), b], v
    
    # same as initial base case, for extra assurance
    return False, None, e, None


def split(e):
    # base case
    if isinstance(e, int):
        if e >= 10:
            return True, [e // 2, math.ceil(e / 2)]
        return False, e
    
    # all other situations, split both sides
    a, b = e
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        # explode until it is not possible anymore
        change, _, x, _ = explode(x)
        if change:
            continue

        # split until it is not possible anymore
        change, x = split(x)
        if not change:
            break
    return x

def magnitude(e):
    if isinstance(e, int):
        return e
    return 3 * magnitude(e[0]) + 2 * magnitude(e[1])

def part_1(data):
    return magnitude(reduce(add, data))

def part_2(data):
    return max(magnitude(add(a, b)) for a, b in permutations(data, 2))

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.readlines()
    data = process_input(data)

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))