import os
import builtins
os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d3 = open('D3.txt', 'r')
# d3 = open('D3test.txt', 'r')

# Part 1
res1 = 0

for ligne in d3:
   l2 = ligne[0:(len(ligne)-2)]
   d = max(l2)
   rk = l2.index(d)
   u = max(ligne[(rk+1):])
   res1 += 10*int(d)+int(u)

print(res1)
# 16946

# Part 2

d3 = open('D3.txt', 'r')
res2 = 0

for ligne in d3:
   l1 = ligne[0:(len(ligne)-1)]
   for k in range(11,-1,-1):
    l2 = l1[0:(len(l1)-k)]
    d = max(l2)
    rk = l2.index(d)
    l1 = l1[(rk+1):]
    res2 += pow(10,k)*int(d)

print(res2)
# 168627047606506
