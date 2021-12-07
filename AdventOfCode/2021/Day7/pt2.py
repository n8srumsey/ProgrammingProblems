# Day7 Part 2 

import statistics 
data_input = "./input.txt"

with open(data_input) as file:
    data = [int(s) for s in file.readline().rstrip('\n').split(',')]
    
def get_average():
    return statistics.mean(data)

def fuel(distance):
    return sum([i for i in range(1, distance + 1)])

def get_fuel(average):
    f = []
    for crab in data:
        f.append(fuel(abs(crab - average)))
    return f

if __name__ == '__main__':
    average = int(get_average())
    print(average)
    fuel1 = get_fuel(average)
    print(sum(fuel1))