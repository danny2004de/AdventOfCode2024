from functools import cache

def blink(stone):
    if stone == '0': 
        return ['1']
    elif len(stone)%2 == 0: 
        half = len(stone)//2
        return [str(int(stone[:half])), str(int(stone[half:]))]
    else:
        return [str(int(stone)*2024)]

@cache 
def fastblink(stone, steps):
    n = blink(stone)
    if steps == 1:
        return len(n)
    return sum(fastblink(s, steps-1) for s in n)

def part1(filename, blinks): 
    f = open(filename, 'r')
    line = f.read().strip()
    print(sum(fastblink(s, blinks) for s in line.split()))
        
def part2(filename, blinks): 
    part1(filename, blinks)

part1('sample', 6)
part1('input', 25)

part2('input', 75)