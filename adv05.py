from functools import total_ordering
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    orderings = []
    pairs = {}
    i = 0
    while lines[i] != '':
        n0, n1 = lines[i].split('|')
        if n1 not in pairs:
            pairs[n1] = [n0]
        else:
            pairs[n1].append(n0)
        i += 1
    i += 1
    out = 0
    while i < len(lines):
        orderings.append(lines[i].split(','))
        i += 1
    for order in orderings:
        for i in range(len(order)):
            if order[i] not in pairs: continue
            for j in range(i+1, len(order)):
                if order[j] in pairs[order[i]]: break
            else: continue
            break
        else: out += int(order[len(order)//2])
    print(out)
    

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    orderings = []
    pairs = {}
    i = 0
    while lines[i] != '':
        n0, n1 = lines[i].split('|')
        if n1 not in pairs:
            pairs[n1] = [n0]
        else:
            pairs[n1].append(n0)
        i += 1
    i += 1
    while i < len(lines):
        orderings.append(lines[i].split(','))
        i += 1
        
    @total_ordering
    class num_comp:
        def __init__(self, s):
            self.s = s
        def __eq__(self, other):
            if self.s in pairs:
                return other.s not in pairs[self.s]
            if other.s in pairs:
                return self.s not in pairs[other.s]
            return True
        def __lt__(self, other):
            if self.s not in pairs: return False
            return other.s in pairs[self.s]
        
    bad_orders = []
    for order in orderings:
        for i in range(len(order)):
            if order[i] not in pairs: continue
            for j in range(i+1, len(order)):
                if order[j] in pairs[order[i]]: break
            else: continue
            break
        else: continue
        bad_orders.append([num_comp(o) for o in order])
    out = 0
    for o in bad_orders:
        o = sorted(o)
        out += int(o[len(o)//2].s)
    print(out)
        
    
        
    
    
          
# part1('sample')
# part1('input')

part2('sample')
part2('input')