# Day5 Part 1 

data_input = "./input.txt"

with open(data_input) as f:
    data = [l.rstrip(('\n')) for l in f.readlines()]
    
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def is_horizontal(self):
        return self.y1 == self.y2
    
    def is_vertical(self):
        return self.x1 == self.x2
        
    def get_points_hv(self):
        points = []
        if self.is_horizontal():
            if self.x1 < self.x2:
                for x in range(self.x1, self.x2+1):
                    points.append({'x': x, 'y':self.y1})
            else:
                for x in range(self.x2, self.x1+1):
                    points.append({'x': x, 'y':self.y1})
        elif self.is_vertical(): 
            if self.y1 < self.y2:
                for y in range(self.y1, self.y2+1):
                    points.append({'x': self.x1, 'y': y})
            else:
                for y in range(self.y2, self.y1+1):
                    points.append({'x': self.x1, 'y': y})
        return points
      
def generate_grid():
    grid = []
    
    for r in range(1000):
        grid.append([])
        for _ in range(1000):
            grid[r].append(0)  
    return grid

def place_hv_lines(grid, lines):
    for line in lines:
        if line.is_horizontal() or line.is_vertical():
            for p in line.get_points_hv():
                grid[p['y']][p['x']] += 1
    return grid

def count_overlaps(grid):
    count = 0
    for r in grid:
        for p in r:
            if p > 1:
                count += 1
    return count

def print_grid(grid):
    for r in grid:
        print(r)
                 

if __name__ == '__main__':   
    
    ### 
    
    lines = []
    for l in data:
        points = l.split(' -> ')
        coords = [[int(c) for c in p.split(',')] for p in points]
        lines.append(Line(coords[0][0], coords[0][1], coords[1][0], coords[1][1]))
        
    #####
    
    grid = generate_grid()
    grid = place_hv_lines(grid, lines)
    
    ### 
    
    n_overlap = count_overlaps(grid)
    print(n_overlap)
    