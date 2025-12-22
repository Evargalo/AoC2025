import os
import builtins
import numpy as np
import math

os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d9 = open('D9.txt', 'r')
# d9 = open('D9test.txt', 'r')

# data
df = d9.read()
m = df.split(sep='\n')
m = m[0:len(m)-1]
m = [[int(a) for a in x.split(',')] for x in m]
print(m[0:3])

# Part 1
max_area = 0
for t1 in m:
    for t2 in m:
        v1 = min(t1[0],t2[0])
        v2 = max(t1[0],t2[0])
        v3 = min(t1[1],t2[1])
        v4 = max(t1[1],t2[1])
        area = (v2-v1+1) * (v4-v3+1)
        if (area > max_area):
            max_area = area
print(max_area)
# 4738108384

# Part 2

borders = [m[0]+m[len(m)-1]]
for i in range(len(m)-1):
    borders.append(m[i]+m[i+1])
v_borders = [[min(x[1],x[3]), max(x[1],x[3]), x[0]] for x in borders if x[0]==x[2]]
h_borders = [[min(x[0],x[2]), max(x[0],x[2]), x[1]] for x in borders if x[1]==x[3]]
print(v_borders[0:10])
print(h_borders[0:10])

max_area = 0
for i in range(len(m)-2):
    t1 = m[i]
    for j in range(i+1,(len(m)-1)):
            t2 = m[j]
            v1 = min(t1[0],t2[0])
            v2 = max(t1[0],t2[0])
            v3 = min(t1[1],t2[1])
            v4 = max(t1[1],t2[1])
            valid = True
            for b in h_borders:
                if( b[0] < v2 and b[1] > v1 and v3 < b[2] and b[2]< v4 ):
                    valid = False
                    break
            for b in v_borders:
                if( b[0] < v4 and b[1] > v3 and v1 < b[2] and b[2] < v2 ):
                    valid = False
                    break
            if(valid):
                area = (v2-v1+1) * (v4-v3+1)
                if (area > max_area):
                    max_area = area
                    # print(v1,v2,v3,v4,area)
print(max_area) 
# 1513792010
