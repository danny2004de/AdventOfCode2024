from itertools import product
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    freqs = {}
    points = {}
    anodes = set()
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            points[(i, j)] = char
            if char != '.':
                if char in freqs:
                    freqs[char].append((i, j))
                else:
                    freqs[char] = [(i, j)]
    for antennae in freqs.values():
        if len(antennae) <= 1: continue
        a_pairs = product(antennae, repeat=2)
        for a, b in a_pairs:
            if a == b: continue
            ax, ay = a
            bx, by = b
            anode1 = (2*bx-ax, 2*by-ay)
            anode2 = (2*ax-bx, 2*ay-by)
            for anode in [anode1, anode2]:
                if anode in points: anodes.add(anode)
    print(len(anodes))

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    freqs = {}
    points = {}
    anodes = set()
    for i, l in enumerate(lines):
        for j, char in enumerate(l):
            points[(i, j)] = char
            if char != '.':
                if char in freqs:
                    freqs[char].append((i, j))
                else:
                    freqs[char] = [(i, j)]
    for antennae in freqs.values():
        if len(antennae) <= 1: continue
        a_pairs = product(antennae, repeat=2)
        for a, b in a_pairs:
            if a == b: continue
            ax, ay = a
            bx, by = b
            for p in points:
                px, py = p
                if (py-by)*(bx-ax) == (by-ay)*(px-bx): 
                    anodes.add(p)
    print(len(anodes))

part1('sample')
part1('input')

part2('sample')
part2('input')