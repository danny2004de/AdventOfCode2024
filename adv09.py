from copy import deepcopy
def part1(filename): 
    f = open(filename, 'r')
    line = f.read().strip()
    blocks = [int(i) for i in line[::2]]
    free_spaces = [int(i) for i in line[1::2]]
    free_spaces.append(0)
    s = [chr(i)*blocks[i] + '😊'*free_spaces[i] for i in range(len(blocks))]
    s = list(''.join(s))
    first_free = 0
    while True: 
        if s[-1] == '😊':
            s.pop()
        try:
            first_free = s.index('😊', first_free)
        except ValueError:
            break
        s[first_free] = s[-1]
        s.pop()
    ans = 0
    for i, c in enumerate(s):
        ans += i*ord(c)
    print(ans)

def part1b(filename):
    f = open(filename, 'r')
    line = f.read().strip()
    blocks = [int(i) for i in line[::2]]
    free_spaces = [int(i) for i in line[1::2]]
    free_spaces.append(0)
    lastid = len(blocks)-1
    n = 0
    ans = 0
    for firstid in range(len(free_spaces)):
        fs = blocks[firstid]
        ans += firstid*(n*fs+fs*(fs-1)//2)
        n += fs
        blocks[firstid] = 0
        while free_spaces[firstid] > 0:
            if blocks[lastid] == 0: 
                break
            s = min(free_spaces[firstid], blocks[lastid])
            ans += lastid*(n*s + s*(s-1)//2)
            free_spaces[firstid] -= s
            blocks[lastid] -= s
            n += s
            if blocks[lastid] == 0: 
                lastid -= 1
    print(ans) 

def part2(filename): 
    f = open(filename, 'r')
    line = f.read().strip()
    blocks = [int(i) for i in line[::2]]
    counted = [False for i in blocks]
    free_spaces = [int(i) for i in line[1::2]]
    free_spaces.append(0)
    n = 0
    ans = 0
    for firstid in range(len(free_spaces)):
        fs = blocks[firstid]
        if not counted[firstid]:
            ans += firstid*(n*fs+fs*(fs-1)//2)
            counted[firstid] = True
        n += fs
        
        while free_spaces[firstid] > 0:
            lastid = len(blocks)-1
            free_size = free_spaces[firstid]
            block_fits = True
            while blocks[lastid] > free_size or counted[lastid]:
                lastid -= 1
                if lastid <= firstid:
                    block_fits = False
                    break
            if not block_fits: 
                n += free_size
                break
            s = blocks[lastid]
            ans += lastid*(n*s + s*(s-1)//2) 
            free_spaces[firstid] -= s
            counted[lastid] = True
            n += s
    print(ans)

part1('sample')
part1('input')

part1b('sample')
part1b('input')

part2('sample')
part2('input')