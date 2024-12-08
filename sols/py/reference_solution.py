import sys
import math
from aoc_lib import read_file

def cansolve(left, right):
    nops = len(right) - 1
    if nops == 0:
        return left == right[0]
    iters = int(math.pow(3, nops))
    opctr = [0]*nops
    for i in range(iters):
        accum = right[0]
        if i != 0:
            jj = nops - 1
            while True:
                opctr[jj] += 1
                if opctr[jj] == 3:
                    opctr[jj] = 0
                    jj-=1
                else:
                    break
        for j in range(nops):
            op = opctr[j]
            if op == 0:
                accum = accum * right[j+1]
            elif op == 1:
                accum = accum + right[j+1]
            else:
                accum = accum * int(math.pow(10, 1+math.floor(math.log10(right[j+1])))) + right[j+1]
        if accum == left:
            return True
    return False
        
            
total = 0
with open(r'ref_good.txt', 'w') as f:
    for l in read_file(r'inputs/d7.txt'):
        l = l.strip()
        (left, right) = l.split(":")
        left = int(left)
        right = [int(x) for x in right.split()]
        if cansolve(left, right):
            print("Can solve", l)
            total += left
            f.write(str(left)+'\n')
print(total)
