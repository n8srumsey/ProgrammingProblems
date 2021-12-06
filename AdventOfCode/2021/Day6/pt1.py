# Day6 Part 1 

data_input = "./input.txt"

with open(data_input) as f:
    data = [l.rstrip('\n') for l in f.readlines()][0]

class Fish:       
    def __init__(self, timer) -> None:
        self.countdown = timer
        
    def advance_day(self):
        if self.countdown == 0:
            self.countdown = 6
            return Fish(8)
        
        self.countdown -= 1
        return None
            
fish = [Fish(int(fish)) for fish in data.split(',')]

if __name__ == '__main__':
    fish = [Fish(int(fish)) for fish in data.split(',')]
    
    for _ in range(80):
        new_fishies = []
        for f in fish:
            new_fish = f.advance_day()
            if new_fish is not None:
                new_fishies.append(new_fish)
        for f in new_fishies:
            fish.append(f)
    
    print(len(fish))