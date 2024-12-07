import queue
def part1(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    ans = 0
    for l in lines:
        val, l = l.split(': ')
        val = int(val)
        nums = [int(n) for n in l.split()]
        running_totals = queue.Queue()
        running_totals.put(nums[0])
        for i, n in enumerate(nums):
            if i == 0: continue
            q_len = running_totals.qsize()
            for j in range(q_len):
                t = running_totals.get()
                t1 = t+n
                t2 = t*n
                if t1 <= val:
                    running_totals.put(t1)
                if t2 <= val:
                    running_totals.put(t2)
        if val in running_totals.queue:
            ans += val
    print(ans)
        

def part2(filename): 
    f = open(filename, 'r')
    lines = f.read().splitlines()
    f = open(filename, 'r')
    lines = f.read().splitlines()
    ans = 0
    for l in lines:
        val, l = l.split(': ')
        val = int(val)
        nums = [int(n) for n in l.split()]
        running_totals = queue.Queue()
        running_totals.put(nums[0])
        for i, n in enumerate(nums):
            if i == 0: continue
            q_len = running_totals.qsize()
            for j in range(q_len):
                t = running_totals.get()
                t1 = t+n
                t2 = t*n
                t3 = int(str(t) + str(n))
                if t1 <= val:
                    running_totals.put(t1)
                if t2 <= val:
                    running_totals.put(t2)
                if t3 <= val:
                    running_totals.put(t3)
        if val in running_totals.queue:
            ans += val
    print(ans)

part1('sample')
part1('input')

part2('sample')
part2('input')