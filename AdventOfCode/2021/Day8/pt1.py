# Day8 Part 1 

data__input = "./input.txt"

with open(data__input) as f:
    data = [l.rstrip('\n') for l in f.readlines()]
    
digit_displays = [l.split(' | ')[1].split(' ') for l in data]


if __name__ == '__main__':
    count = 0
    for display in digit_displays:
        for digit in display:
            length  = len(digit)
            if length == 2 or length == 3 or length == 4 or length == 7:
                count += 1
                
    print(count)