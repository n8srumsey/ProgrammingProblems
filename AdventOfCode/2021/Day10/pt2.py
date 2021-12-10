# Day10 Part 2 
from collections import defaultdict

data_input = "./input.txt"

with open(data_input) as file:
    data = [l.rstrip('\n') for l in file.readlines()]

points = {')': 1, ']': 2, '}': 3, '>': 4, '': 0}
close_to_open = {')': '(', ']': '[', '}': '{', '>': '<', '': ''}

open_to_close = defaultdict(list) 
for k, v in close_to_open.items(): 
    open_to_close[v].append(k)

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

def remove_corrupted(data_in):
    data_out = [l for l in data_in if get_first_corrupted(l) == '']
    return data_out

def get_score(completion):
    score = 0
    for c in completion:
        score *= 5
        score += points[c]
    return score

def get_completion(line: str):
    completion = []
    opened = []
    for c in line:
        if c in close_to_open.values():
            opened.append(c)
        else:
            opened, _ = close(opened, c)

    for c in reversed(opened):
        completion.append(open_to_close[c])
    completion = [c[0] for c in completion]
    return completion

if __name__ == '__main__':
    data = remove_corrupted(data)
    scores = []

    for line in data:
        value =  get_score(get_completion(line))
        scores.append(value)

    scores = sorted(scores)
    print(scores[int(len(scores) / 2)])