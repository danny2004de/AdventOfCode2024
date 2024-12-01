import numpy as np
from collections import Counter
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    l1 = [int(line.split()[0]) for line in lines]
    l2 = [int(line.split()[1]) for line in lines]
    l1 = sorted(l1)
    l2 = sorted(l2)
    print(np.sum(np.abs(np.array(l1) - np.array(l2))))

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    l1 = [int(line.split()[0]) for line in lines]
    l2 = [int(line.split()[1]) for line in lines]
    c = Counter(l2)
    sum = 0
    for n in l1:
        sum += n*c[n]
    print(sum)
    
    
# part1('input')
part2('input')