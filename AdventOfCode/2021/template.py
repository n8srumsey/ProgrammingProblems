import utils

def process_input(data):
    return data

def part_1(data):
    pass

def part_2(data):
    pass

if __name__ == '__main__':
    utils.TESTING = True

    # data = utils.readlines()
    # data = utils.readlines_no_strip()
    # data = utils.read_whole_input()
    # data = utils.read_grid_2darray()
    # data = utils.read_dict_input()
    # data = utils.read_nparray_from_digits()
    
    data = process_input(data)
    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))