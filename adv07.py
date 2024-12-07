from itertools import product
from operator import add, mul
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    ans = 0
    for l in lines:
        val, l = l.split(': ')
        val = int(val)
        nums = [int(n) for n in l.split()]
        for p in product([add, mul], repeat=len(nums)-1):
            rtotal = nums[0]
            for n in range(1, len(nums)):
                rtotal = p[n-1](rtotal, nums[n])
                if rtotal > val: break
            if rtotal == val:
                ans += val
                break
    print(ans)
        

def part2(filename): 
    def concat(a, b): return int(str(a)+str(b))
    f = open(filename, 'r')
    lines = f.read().splitlines()
    ans = 0
    for l in lines:
        val, l = l.split(': ')
        val = int(val)
        nums = [int(n) for n in l.split()]
        for p in product([add, mul, concat], repeat=len(nums)-1):
            rtotal = nums[0]
            for n in range(1, len(nums)):
                rtotal = p[n-1](rtotal, nums[n])
                if rtotal > val: break
            if rtotal == val:
                ans += val
                break
    print(ans)

part1('sample')
part1('input')

part2('sample')
part2('input')