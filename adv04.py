
def part1(filename): 
    
    f = open(filename, 'r')
    lines = f.read().splitlines()
    d = {'X': 'M', 'M': 'A', 'A': 'S', 'S': ''}
    def search(p, dir, char):
        x = p[0] + dir[0]
        y = p[1] + dir[1]
        if x < 0 or x > len(lines) - 1 or y < 0 or y > len(lines[0]) - 1: return False
        if lines[x][y] == char:
            if d[char] == '':
                return True
            return search((x, y), dir, d[char])
        return False
    count = 0
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            if char == 'X':
                for d0 in [-1, 0, 1]:
                    for d1 in [-1, 0, 1]:
                        if search((i, j), (d0, d1), 'M'): count += 1
    print(count)
    

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    count = 0
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[0])-1):
            char = lines[i][j]
            if char == 'A':
                s1 = lines[i-1][j-1] + char + lines[i+1][j+1]
                s2 = lines[i-1][j+1] + char + lines[i+1][j-1]
                if s1 in ['MAS', 'SAM'] and s2 in ['MAS', 'SAM']:
                    count += 1               
    print(count)
    
          
# part1('sample')
# part1('input')

part2('sample')
part2('input')