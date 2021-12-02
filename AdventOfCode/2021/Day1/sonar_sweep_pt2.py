input_path = "./sonar_sweep_input.txt"

measurements = []

with open(input_path) as f:
    measurements = f.readlines()
    measurements = [int(m.rstrip()) for m in measurements]
    
count = 0

for i in range(3, len(measurements)):
    if (measurements[i - 3] + measurements[i - 2] + measurements[i - 1] < measurements[i - 2] + measurements[i - 1] + measurements[i]):
        count += 1
        
print(count)