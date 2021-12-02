# Day2 Part 2 

data_path = "./input.txt"

with open(data_path) as f:
    data = f.readlines()
    
ribbon = 0

for p in data:
    x = int(p[:p.find('x')])
    p = p[p.find('x') + 1 :]
    y = int(p[:p.find('x')])
    p = p[p.find('x') + 1 :]
    z = int(p)
    xyz = [x, y, z]
    ribbon += x * y * z + 2 * (sorted(xyz)[0] + sorted(xyz)[1])
print (ribbon)