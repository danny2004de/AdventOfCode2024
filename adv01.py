import numpy as np
from collections import Counter
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    l1, l2 = [], []
    for line in lines:
        k = line.split()
        l1.append(int(k[0]))
        l2.append(int(k[1]))
    l1 = sorted(l1)
    l2 = sorted(l2)
    s = 0
    for i in range(len(lines)):
        s += abs(l1[i] - l2[i])
    print(s)

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    l1, l2 = [], []
    for line in lines:
        k = line.split()
        l1.append(int(k[0]))
        l2.append(int(k[1]))
    c = Counter(l2)
    sum = 0
    for n in l1:
        sum += n*c[n]
    print(sum)
    
    
part1('input')
part2('input')