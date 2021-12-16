import sys
sys.path.append('./..')
import utils

# to binary
def process_input(data):
    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    bin_data = ''
    for c in data[0]:
        bin_data += hex_to_bin[c]
    return bin_data

def bin_to_dec(bin):
    dec = 0
    for i, b in enumerate(reversed(bin)):
        dec += 2 ** i * int(b)
    return dec

def sum_packets(values):
    return sum (values)

def product_packets(values):
    p = 1
    for v in values:
        p *= v
    return p

def min_packets(values):
    return min(values)

def max_packets(values):
    return max(values)

def greater_packets(values):
    return values[0] > values[1]

def less_packets(values):
    return values[0] < values[1]

def equal_packets(values):
    return values[0] == values[1]

operators = {
    0:sum_packets,
    1:product_packets, 
    2:min_packets,
    3:max_packets,
    5:greater_packets,
    6:less_packets,
    7:equal_packets,
}

def parse_transmission(inpt):
    V = bin_to_dec(inpt[:3])
    T = bin_to_dec(inpt[3:6])

    if T == 4:
        length = 11
        binary = ''
        literal = inpt[6:]
        while literal[0] != '0':
            length += 5
            binary += literal[1:5]
            literal = literal[5:]
        binary += literal[1:5]
        num = bin_to_dec(binary)
        return V, length
    
    else:
        total_length = 0
        V_sum = V
        I = inpt[6]
        if I == '0':
            L = bin_to_dec(inpt[7:22])
            length = 0
            while length < L:
                v, l = parse_transmission(inpt[22 + length:])
                V_sum += v
                length += l
            total_length += 22 + L
            return V_sum, total_length
        else: 
            L = bin_to_dec(inpt[7:18])
            length = 0
            for _ in range(L):
                v, l = parse_transmission(inpt[18 + length:])
                V_sum += v
                length += l
            total_length += 18 + length
            return V_sum, total_length

def parse_transmission2(inpt):
    V = bin_to_dec(inpt[:3])
    T = bin_to_dec(inpt[3:6])

    if T == 4:
        length = 11
        binary = ''
        literal = inpt[6:]
        while literal[0] != '0':
            length += 5
            binary += literal[1:5]
            literal = literal[5:]
        binary += literal[1:5]
        value = bin_to_dec(binary)
        return V, value, length
    
    else:
        total_length = 0
        V_sum = V
        I = inpt[6]
        sub_values = []
        if I == '0':
            L = bin_to_dec(inpt[7:22])
            length = 0
            while length < L:
                v, val, l = parse_transmission2(inpt[22 + length:])
                V_sum += v
                length += l
                sub_values.append(val)
            total_length += 22 + L
            return V_sum, operators[T](sub_values), total_length
        else: 
            L = bin_to_dec(inpt[7:18])
            length = 0
            for _ in range(L):
                v, val, l = parse_transmission2(inpt[18 + length:])
                V_sum += v
                length += l
                sub_values.append(val)
            total_length += 18 + length
            return V_sum, operators[T](sub_values), total_length

def part_1(data):
    sum_versions, _ = parse_transmission(data)
    return sum_versions


def part_2(data):
    _, val, _ = parse_transmission2(data)
    return val

if __name__ == '__main__':
    utils.TESTING = False

    data = utils.readlines()
    data = process_input(data)

    print('Part 1:', part_1(data))
    print('Part 2:', part_2(data))