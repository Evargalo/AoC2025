import os
import builtins

os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')

# Data
d5_ranges = open('D5_ranges.txt', 'r')
d5_ids = open('D5_ids.txt', 'r')
ingredients = d5_ids.read().split(sep='\n')
ingredients = [int(x) for x in ingredients if x!='']

def read_range(r):
     r1,r2 = r.split(sep='-')
     ir1 = int(r1)
     ir2 = int(r2)
     return(ir1,ir2)

# Part 1
res = set() # set of fresh ingredients
for r in d5_ranges:
    ir1, ir2 = read_range(r)
    res = res.union(set([x for x in ingredients if x >= ir1 and x <= ir2]))
print(len(res))
# 664

# Part 2
final_range = set() # the aggregated ranges
d5_ranges.seek(0)

for r in d5_ranges:
    new_range = set() # which ranges we keep at this step
    for fr in final_range:
        ir1, ir2 = read_range(r)
        ifr1, ifr2 = read_range(fr)
        if((ir2 < ifr1-1) | (ifr2 < ir1-1)): # no intersection
            new_range.add(fr)
        else: # collapse the 2 ranges
            r = str(min(ir1,ifr1)) + '-' + str(max(ir2,ifr2))
    new_range.add(r)
    final_range = new_range

res = 0 
for fr in final_range:
    ifr1, ifr2 = read_range(fr)
    res += ifr2 - ifr1 + 1
print(res)
# 350780324308385