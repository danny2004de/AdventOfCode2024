import numpy as np
from collections import Counter
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    count = 0
    for l in lines:
        l = l.split()
        k = np.diff(np.array(l, dtype=int))
        if np.all(np.isin(k, [-1, -2, -3])):
            count += 1
        if np.all(np.isin(k, [1, 2, 3])):
            count += 1
    print(count)

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    count = 0
    for l in lines:
        l = l.split()
        for i in range(len(l)):
            j = l.copy()
            j.pop(i)
            k = np.diff(np.array(j, dtype=int))
            if np.all(np.isin(k, [-1, -2, -3])):
                count += 1
                break
            if np.all(np.isin(k, [1, 2, 3])):
                count += 1
                break
    print(count)
      
part1('sample')
part1('input')

part2('sample')
part2('input')