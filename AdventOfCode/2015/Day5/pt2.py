# Day5 Part 2 

import re

data_path = "./input.txt"

with open(data_path) as f:
    strings = f.readlines()
    
nice = 0

dupl = re.compile(r"\b\w*(\w{2})\w*\1")
between = re.compile(r"(.)(.)\1")

for s in strings:

    n = True
    
    if not re.findall(dupl, s):
        n = False
        
    if not re.search(between, s):
        n = False
        
    if n:
        nice += 1
        
print(nice)