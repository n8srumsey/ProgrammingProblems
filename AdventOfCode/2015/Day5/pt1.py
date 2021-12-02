# Day5 Part 1 

import re

data_path = "./input.txt"

with open(data_path) as f:
    strings = f.readlines()
    
nice = 0

dupl = re.compile(r"(.)\1")
cont = re.compile(r"(ab)|(cd)|(pq)|(xy)")

for s in strings:
    n_vowels = len(re.findall('[aeiou]', s, re.IGNORECASE))
    n = True
    
    if n_vowels < 3:
        n = False
    
    if not re.search(dupl, s):
        n = False
        
    if re.search(cont, s):
        n = False
        
    if n:
        nice += 1
        
print(nice)