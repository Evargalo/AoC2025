import os
import builtins
import numpy as np
import math

os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d6 = open('D6.txt', 'r')
# d6 = open('D6test.txt', 'r')

# data
df = d6.read()
m = df.split(sep='\n')
m = m[0:len(m)-1]
m = [x.split() for x in m]
homework = np.array(m).transpose()

# Part 1
res = 0
for h in homework:
    ope = h[len(h)-1]
    vals = [int(x) for x in h[0:len(h)-1]]
    if(ope == "*"):
        res += math.prod(vals)
    if(ope == "+"):
        res += sum(vals)
print(res)
# 7326876294741

# Part 2
m = df.split(sep='\n')
m = m[0:len(m)-1]
m = [list(x) for x in m]
if(len(m[len(m)-1]) < len(m[0])):
    m[len(m)-1].append(' ')
homework = np.array(m).transpose()

res = 0
vals = []
ope = ''
for h in homework:
    h = ''.join(h).split()
    h = ''.join(h)
    if (ope == ''):
        ope = h[len(h)-1]
        h = h[0:len(h)-1]
    if(h == ''):
        if(ope == "*"):
            res += math.prod(vals)
        if(ope == "+"):
            res += sum(vals)
        vals = []
        ope = ''
    else:
        vals.append(int(h))
# dernière opération
if(ope == "*"):
    res += math.prod(vals)
if(ope == "+"):
    res += sum(vals)
print(res)
# 10756006415204