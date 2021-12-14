import sys
from typing import Counter
sys.path.append('./..')
import utils
import collections

def process_input(data):
    inpt = {'template': '', 'rules': {}}
    inpt['template'] = data[0]
    data = data[2:]

    for l in data:
        pair = l.split(' -> ')[0]
        insertion = l.split(' -> ')[1]
        inpt['rules'][pair] = insertion
    
    return inpt

def apply_rules(pairs, rules):
    new_pairs = {}
    for pair, frequency in pairs.items():
      insertion = rules[pair[0] + pair[1]]
      l = pair[0] + insertion
      r = insertion + pair[1]
      if l in new_pairs:
        new_pairs[l] += frequency
      else:
        new_pairs[l] = frequency
      
      if r in new_pairs:
        new_pairs[r] += frequency
      else:
        new_pairs[r] = frequency
    return new_pairs   

def calculate_diff(pairs, template):
    letters = {}
    for pair, frequency in pairs.items():
        l = pair[0]
        r = pair[1]
        if l in letters:
            letters[l] += frequency
        else:
            letters[l] = frequency
        
        if r in letters:
            letters[r] += frequency
        else:
            letters[r] = frequency
    letters[template[0]] += 1
    letters[template[-1]] += 1

    # divide by two because everything is double counted
    return (max(letters.values()) - min(letters.values())) // 2

def part_1(data):
    template = data['template']
    rules = data['rules']

    pairs = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1

    n_steps = 10
    for _ in range(n_steps):
        pairs = apply_rules(pairs, rules)
    
    return calculate_diff(pairs, template)

def part_2(data):
    template = data['template']
    rules = data['rules']

    pairs = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    n_steps = 40
    for _ in range(n_steps):
        pairs = apply_rules(pairs, rules)
    
    return calculate_diff(pairs, template)

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.readlines()
    data = process_input(data)

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))