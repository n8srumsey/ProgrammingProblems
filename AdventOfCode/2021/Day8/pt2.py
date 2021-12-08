# Day8 Part 2 

data__input = "./input.txt"

with open(data__input) as f:
    data = [l.rstrip('\n') for l in f.readlines()]
    
digit_displays = [[x.split(' ') for x  in l.split(' | ') ] for l in data]

def num_from_chars(chars, chars_to_nums):
    for digit in chars_to_nums:
        if chars_to_nums[digit] == set(chars):
            return digit



known_lengths = {2: 1, 3: 7, 4: 4, 7: 8}

if __name__=='__main__':
    answer = 0
    for dislpay in digit_displays:
        lhs, rhs = dislpay[0], dislpay[1]
        signal_patterns = lhs + rhs
        
        letters_to_numbers = {}
        letters_to_numbers[1] = set()
        letters_to_numbers[8] = set()
        letters_to_numbers[4] = set()
        letters_to_numbers[7] = set()
        
        for digit in signal_patterns:
            if len(digit) in known_lengths:
                letters_to_numbers[known_lengths[len(digit)]] = set(digit)
        
        for digit in signal_patterns:
            if len(digit) == 5 and letters_to_numbers[1].intersection(digit) == letters_to_numbers[1]:
                letters_to_numbers[3] = set(digit)
        
        top = letters_to_numbers[7] - letters_to_numbers[1]
        middle = letters_to_numbers[3].intersection(letters_to_numbers[4] - letters_to_numbers[1])
        top_left = (letters_to_numbers[4] - letters_to_numbers[1]) - set(middle)

        for digit in signal_patterns:
            if len(digit) == 5 and set(digit) != letters_to_numbers[3]:
                if top_left.intersection(digit) == set():
                    letters_to_numbers[2] = set(digit)
                else:
                    letters_to_numbers[5] = set(digit)
            
            if len(digit) == 6:
                if set(digit).intersection(set(middle)) == set():
                    letters_to_numbers[0] = set(digit)
                elif set(digit).intersection(letters_to_numbers[1]) == letters_to_numbers[1]:
                    letters_to_numbers[9] = set(digit)
                else:
                    letters_to_numbers[6] = set(digit)

        num = ''
        for digit in rhs:
            num += str(num_from_chars(digit, letters_to_numbers))
        answer += int(num)
    
    print("ANSWER: ", answer)