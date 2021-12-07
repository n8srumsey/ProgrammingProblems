# Day7 Part 1 
import statistics 
data_input = "./input.txt"

with open(data_input) as file:
    data = [int(s) for s in file.readline().rstrip('\n').split(',')]
    
def get_average():
    return statistics.median(data)

def get_fuel(average):
    fuel = []
    for crab in data:
        fuel.append(abs(crab - average))
    return fuel

if __name__ == '__main__':
    average = int(get_average())
    print(average)
    fuel = get_fuel(average)
    print(sum(fuel))