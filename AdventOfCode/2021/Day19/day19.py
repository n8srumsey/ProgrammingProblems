import sys
sys.path.append('./..')
import utils

ROTATIONS = [
    ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
    ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
    ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
    ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
    ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
    ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
    ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
    ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),
    ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
    ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
    ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
    ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
    ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
    ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
    ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
    ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
    ((0, 1, 0), (0, 0, -1), (-1, 0, 0)),
    ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
    ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
    ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
    ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
    ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
]


class Scanner:
    def __init__(self, n_id, coords) -> None:
        self.id = n_id
        self.coords = coords

    def print(self):
        print(f'--- scanner {self.id} ---')
        for c in self.coords:
            print(','.join(map(str, c)))

    def gen_alt_orientations(self):
        def rotate(x_rot, y_rot, z_rot):
            new_coords = []
            for c in self.coords:
                x = sum(a * b for a, b in zip(c, x_rot))
                y = sum(a * b for a, b in zip(c, y_rot))
                z = sum(a * b for a, b in zip(c, z_rot))
                new_coords.append((x, y, z))
            return Scanner(self.id, new_coords)

        for rot in ROTATIONS:
            yield rotate(*rot)


def find_scanner_match(known, scanners):
    for scanner in scanners.values():
        for orientation in scanner.gen_alt_orientations():
            test_coords = list(orientation.coords)
            for base_c in known.coords:
                for i, test_c in enumerate(orientation.coords):
                    if i+11 >= len(test_coords):
                        # Not enough left to find a match
                        break
                    x_offset, y_offset, z_offset = (a-b for a, b in zip(base_c, test_c))
                    x, y, z = test_c
                    c = (x + x_offset, y + y_offset, z + z_offset)
                    matches = 1
                    for c in test_coords[i+1:]:
                        x, y, z = c
                        c2 = (x+x_offset, y+y_offset, z+z_offset)
                        if c2 in known.coords:
                            matches += 1
                    if matches >= 12:
                        match_coords = [(x+x_offset, y + y_offset, z + z_offset) for x, y, z in orientation.coords]
                        orientation.coords = set(match_coords)
                        del scanners[scanner.id]
                        return orientation, (x_offset, y_offset, z_offset)
    assert False


def process_input(data):
    scanners = {}
    groups = data.split('\n\n')
    for i, scanner in enumerate(groups):
        lines = scanner.splitlines()
        coords = []
        for line in lines[1:]:
            coords.append(tuple(map(int, line.split(','))))
        scanners[i] = Scanner(i, set(coords))
    return scanners
    
def part_1(scanners):
    known = scanners[0]
    del scanners[0]

    while len(scanners):
        match, _ = find_scanner_match(known, scanners)
        known.coords |= match.coords
    
    return len(known.coords)

def part_2(scanners):
    known = scanners[0]
    del scanners[0]

    offsets = [(0,0,0)]

    while len(scanners):
        match, offset = find_scanner_match(known, scanners)
        known.coords |= match.coords
        offsets.append(offset)

    answer = 0

    for offset0 in offsets:
        for offset1 in offsets:
            dist = sum(abs(a - b) for a, b in zip(offset0, offset1))
            answer = max(answer, dist)
    return answer

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.read_whole_input()
    data1 = process_input(data)
    data2 = process_input(data)
    print('Part 1:', part_1(data1))
    print('Part 2:', part_2(data2))