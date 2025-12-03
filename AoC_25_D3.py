import os
import builtins
os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')

def pick_batteries(nb_digits) -> int: 
    d3 = open('D3.txt', 'r')
    res = 0
    for ligne in d3:
        l1 = ligne[0:(len(ligne)-1)]
        for k in range(nb_digits-1,-1,-1):
            l2 = l1[0:(len(l1)-k)]
            d = max(l2)
            rk = l2.index(d)
            l1 = l1[(rk+1):]
            res += pow(10,k)*int(d)
    return res

# Part 1
print(pick_batteries(2))
#16946

# Part 2
print(pick_batteries(12))
# 168627047606506