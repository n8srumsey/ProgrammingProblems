# Day7 Part 1 

"""data_input = "./input.txt"

with open(data_input) as f:
    commands = [l.rstrip('\n') for l in f]

circuit = {}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for l1 in alphabet:
    circuit[l1] = 0
    for l2 in alphabet:
        circuit[(l1 + l2)] = 0

for c in commands:
    line = c.split(' -> ')
    lvalue = line[0]
    rvalue = line[1]
    v = 0

    if 'AND' in lvalue:
        values = lvalue.split(' AND ')
        if values[0].isdigit():
            v = int(values[0]) & circuit[values[1]]
        else:
            v = circuit[values[0]] & circuit[values[1]]
    
    elif 'OR' in lvalue:
        values = lvalue.split(' OR ')
        v = circuit[values[0]] | circuit[values[1]]
     
    elif 'LSHIFT' in lvalue:
        values = lvalue.split(' LSHIFT ')
        v = circuit[values[0]] << int(values[1])
     
    elif 'RSHIFT' in lvalue:
        values = lvalue.split(' RSHIFT ')
        v = circuit[values[0]] >> int(values[1])
     
    elif 'NOT' in lvalue:
        values = lvalue.split()
        v = ~ circuit[values[1]]

    else:
        if lvalue.isdigit():
            v = int(lvalue)
        else:
            v = circuit[lvalue]

    if v < 0:
        v += 65536    

    circuit[rvalue] = v
    

print(circuit['a'])"""

import re

data_input = "./input.txt"

with open(data_input) as f:
    commands = [l.rstrip('\n') for l in f]

monops = {
    'NOT': lambda x : ~x & 0xFFFF,
}

binops = {
    'AND': lambda x, y : x & y,
    'OR': lambda x, y : x | y,
    'LSHIFT': lambda x, y : x << y,
    'RSHIFT': lambda x, y : x << y,
}

machine = {}

for line in commands:
    m = (
        re.match(r'(\w+) -> (\w+)', line)
        or re.match(r'(\w+) (\w+) (\w+) -> (\w+)', line)
        or re.match(r'(\w+) (\w+) -> (\w+)', line)
    ).groups()

    machine[m[-1]] = m[:-1]

def evaluate(register_or_value):
    try:
        return int(register_or_value)
    except:
        return run(register_or_value)

def run(register, state = {}):
    if not register in state:
        command = machine[register]

        if len(command) == 1:
            value, = command
            state[register] = evaluate(value)

        elif len(command) == 2:
            monop, input = command
            state[register] = monops[monop](evaluate(input))

        elif len(command) == 3:
            input_1, binop, input_2 = command
            state[register] = binops[binop](evaluate(input_1), evaluate(input_2))

    return state[register]


print(run('a'))