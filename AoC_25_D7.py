import os
import builtins
import numpy as np
import math

os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d7 = open('D7.txt', 'r')
# d7 = open('D7test.txt', 'r')

# data
df = d7.read()
m = df.split(sep='\n')
m = m[0:len(m)-1]
beam = m[0].find('S')

# Part A
beams=[beam]
nb_splits = 0
for line in m[1:len(m)]:
    if(line.find('^')==-1):
        next
    new_timelines = []
    for b in beams:
        if(line[b]=='.' and not(b in new_timelines)):
            new_timelines.append(b)
        if(line[b]=='^'):
            nb_splits += 1
            if(not(b-1 in new_timelines)):
                new_timelines.append(b-1)
            new_timelines.append(b+1)
    beams = new_timelines

print(beams)
print(nb_splits)
# 1651

# Part B
        
timelines = [[beam,1]]

for line in m[1:len(m)]:
    if(line.find('^') != -1):
        new_timelines = []
        for t in timelines:
            b = t[0]
            if(line[b]=='.'):
                if(len(new_timelines) == 0):
                    new_timelines.append(t)
                elif(new_timelines[len(new_timelines)-1][0] == b):
                    new_timelines[len(new_timelines)-1][1] += t[1]
                else:
                    new_timelines.append(t)
            if(line[b]=='^'):
                if(len(new_timelines) == 0):
                    new_timelines.append([b-1,t[1]])
                elif(new_timelines[len(new_timelines)-1][0] == b-1):
                    new_timelines[len(new_timelines)-1][1] += t[1]
                else:
                    new_timelines.append([b-1,t[1]])
                new_timelines.append([b+1,t[1]])
        timelines = new_timelines

nb_universes = 0
for t in timelines:
    nb_universes += t[1]
print(nb_universes)
# 108924003331749

