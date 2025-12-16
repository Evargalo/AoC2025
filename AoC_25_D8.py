import os
import builtins
import numpy as np
import math

os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d8 = open('D8.txt', 'r')
# d8 = open('D8test.txt', 'r')

# data
df = d8.read()
m = df.split(sep='\n')

def dist(a,b):
    return( pow( pow(a[0]-b[0],2) + pow(a[1]-b[1],2) + pow(a[2]-b[2],2)  , 1/2) )

spots = list()
for spot in m:
     spot = spot.split(',')
     spot = [x for x in spot if x!='']
     spot = [int(x) for x in spot]
     if(len(spot) == 3):
         spots.append(spot)

tab_dist = list()
for i in (range(len(spots))):
     for j in (range(len(spots))):
        if(i != j):
            tab_dist.append([i,j,dist(spots[i],spots[j])])

# Part A
 
nb_connexions = 1000
# nb_connexions = 10
def get_third(l):
    return(l[2])

tab_dist.sort(key=get_third)
prov_links = tab_dist[0:(2*nb_connexions)]
links= [prov_links[i] for i in range(len(prov_links)) if i % 2 == 0 ]

spots_nums = range(len(spots))
circuits = [[i] for i in spots_nums]

for l in links:
    for c in circuits:
        if l[0] in c:
            c1 = c        
        if l[1] in c:
            c2 = c
    if c1 != c2:
        new_c = c1 + c2
        circuits.remove(c1)
        circuits.remove(c2)
        circuits.append(new_c)

circuits.sort(key = len, reverse=True)
lc = [len(c) for c in circuits[0:3]]
print(lc)
print(math.prod(lc))
# 163548

# Part B

circuits = [[i] for i in spots_nums]
nb_useful_links = 0
print("Part B")
print("Goal =")
print(len(spots))
for l in tab_dist:
    for c in circuits:
        if l[0] in c:
            c1 = c        
        if l[1] in c:
            c2 = c
    if c1 != c2:
        new_c = c1 + c2
        circuits.remove(c1)
        circuits.remove(c2)
        circuits.append(new_c)
        nb_useful_links += 1
        if(nb_useful_links % 100 ==0):
            print(nb_useful_links)
        if(nb_useful_links == len(spots)-1):
            last_connexion = l
            break

x1 = spots[last_connexion[0]]
x2 = spots[last_connexion[1]]
print(x1[0] * x2[0])
# 772452514
