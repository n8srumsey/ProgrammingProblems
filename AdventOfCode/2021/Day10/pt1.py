# Day10 Part 1 

data_input = "./input.txt"

with open(data_input) as file:
    data = [l.rstrip('\n') for l in file.readlines()]

points = {')': 3, ']': 57, '}': 1197, '>': 25137, '': 0}
close_to_open = {')': '(', ']': '[', '}': '{', '>': '<', '': ''}

def is_complete(line: str):
    if line.count('(') != line.count(')'):
        return False
    if line.count('[') != line.count(']'):
        return False
    if line.count('{') != line.count('}'):
        return False
    if line.count('<') != line.count('>'):
        return False
    return True

def get_first_corrupted(line: str):
    opened = []
    for c in line:
        if c in close_to_open.values():
            opened.append(c)
        else:
            opened, char = close(opened, c)
            if char is not None:
                return char
    return ''

def close(opened, char: str):
    if opened[-1] == close_to_open[char]:
        opened.pop()
        return opened, None
    return opened, char

if __name__ == '__main__':
    answer = 0

    for line in data:
        # if is_complete(line):
        value =  points[get_first_corrupted(line)]
        answer += value

    print(answer)