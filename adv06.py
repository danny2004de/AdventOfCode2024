from itertools import cycle
from copy import deepcopy
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            if char == '^':
                x, y = i, j
                break
        else: continue
        break
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = 0
    dx, dy = dirs[dir_index%4]
    positions = set()
    positions.add((x, y))
    while -1 < x + dx < len(lines) and -1 < y+dy < len(lines[0]):
        char = lines[x+dx][y+dy]
        if char != '#':
            x = x + dx
            y = y + dy
            positions.add((x, y))
        else:
            dir_index += 1
            dx, dy = dirs[dir_index%4]
    print(len(positions))
    return positions
            

    

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            if char == '^':
                start = (i, j)
                break
        else: continue
        break
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def check_loop(stage):
        x, y = start
        dir_index = 0
        dx, dy = dirs[dir_index%4]
        positions = set()
        while -1 < x + dx < len(stage) and -1 < y+dy < len(stage[0]):
            if (x, y, dx, dy) in positions:
                return True
            char = stage[x+dx][y+dy]
            if char != '#':
                positions.add((x, y, dx, dy))
                x += dx
                y += dy
            else:
                dir_index += 1
                dx, dy = dirs[dir_index%4]
        return False
    visited_positions = part1(filename)
    count = 0
    st = [list(k) for k in lines]
    for i, j in visited_positions:
        if (i, j) == start: continue
        s = deepcopy(st)
        s[i][j] = '#'
        if check_loop(s):
            count += 1
    print(count)
        
    
        
    
    
          
part1('sample')
part1('input')

part2('sample')
part2('input')