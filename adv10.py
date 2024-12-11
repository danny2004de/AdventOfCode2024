def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    points = {}
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            points[(i, j)] = int(char)
    heads = [p for p in points if points[p]==0]
    ans = 0
    def search(p):
        n = points[p]
        if n == 9: return [p]
        i, j = p
        out = []
        for s in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if s in points and points[s] == n+1:
                out += search(s)
        return out
    for h in heads:
        ans += len(set(search(h)))
    print(ans)

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    points = {}
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            points[(i, j)] = int(char)
    heads = [p for p in points if points[p]==0]
    ans = 0
    def search(p):
        n = points[p]
        if n == 9: return 1
        i, j = p
        out = 0
        for s in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if s in points and points[s] == n+1:
                out += search(s)
        return out
    for h in heads:
        ans += search(h)
    print(ans)

part1('sample')
part1('input')

part2('sample')
part2('input')