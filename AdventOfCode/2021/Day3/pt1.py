data_input = "./input.txt"

with open(data_input) as f:
    data = [l.rstrip("\n") for l in f.readlines()]

cols = [[] for _ in range(len(data[0]))]
for l in data:
    for i, c in enumerate(l):
        cols[i].append(c)

columns = ["".join(cols[i]) for i in range(len(cols))]
gamma = ""
epsilon = ""
for i in columns:
    freq_0 = 0
    freq_1 = 0
    
    for s in i:
        if s == "1":
            freq_1 += 1
        else: 
            freq_0 += 1
    
    if freq_0 > freq_1:
        gamma += "0"
        epsilon += "1"
    if freq_1 > freq_0:
        epsilon += "0"
        gamma += "1"

print(int(gamma, 2) * int(epsilon, 2))