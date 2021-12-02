# Day2 Part 1 

data_path = "./input.txt"

with open(data_path) as f:
    data = f.readlines()
    
sqftwp = 0

for p in data:
    x = int(p[:p.find('x')])
    p = p[p.find('x') + 1 :]
    y = int(p[:p.find('x')])
    p = p[p.find('x') + 1 :]
    z = int(p)
    sqftwp += 2 * (x * y + y * z + z * x) + min(x * y, y * z, z * x)
print (sqftwp)