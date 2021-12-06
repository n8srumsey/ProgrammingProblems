# Day6 Part 2 
data_input = "./input.txt"

with open(data_input) as file:
    data = [int(f) for f in file.readline().strip().split(',')]

if __name__ == '__main__':
    cycle_count = [0 for _ in range(10)]

    for time in data:
        cycle_count[time] += 1

    total_days = 256
    for day in range(total_days):
        for i, count in enumerate(cycle_count):
            if i == 0:
                cycle_count[7] += count
                cycle_count[9] += count
                cycle_count[i] = 0
            else:
                cycle_count[i - 1] += count
                cycle_count[i] = 0
                
    print(cycle_count)