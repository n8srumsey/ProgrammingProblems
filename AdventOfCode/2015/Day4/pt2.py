# Day4 Part 2 
 
from itertools import count
from hashlib import md5

key = 'ckczppom'

for i in count():
    h = key + str(i)
    if md5(h.encode()).hexdigest()[:5] == '000000':
        print(i)
        break
