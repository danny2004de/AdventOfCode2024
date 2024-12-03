import re
def part1(filename): 
    f = open(filename, 'r')
    line = f.read()
    l = re.findall('mul\(\d+,\d+\)', line)
    print(l)
    sum = 0
    for i in l:
        k = i.split(',')
        sum += int(k[0][4:])*int(k[1][:-1])
    print(sum)
    
    

def part2(filename): 
    f = open(filename, 'r')
    line = f.read()
    # p = re.compile('mul\(\d+,\d+\)|(do\(\)|don\'t\(\))')
    l = re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
    print(l)
    do = True
    sum = 0
    for i in l:
        if i == "don't()":
            do = False
        elif i == 'do()':
            do = True
        elif do:
            k = i.split(',')
            sum += int(k[0][4:])*int(k[1][:-1])
    print(sum)
      
part1('sample')
part1('input')

part2('sample')
part2('input')