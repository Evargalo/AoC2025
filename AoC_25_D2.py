import os
import builtins
os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d2 = open('D2.txt', 'r')
# d2 = open('D2test.txt', 'r')
l = d2.read().split(sep=',')

# Part 1

res = 0
for plage in l:
    r = plage.split(sep='-')
    s1 = r[0]
    r1 = int(s1)
    r2 = int(r[1])
    if(len(s1) % 2 == 0):
        coupe = len(s1) // 2
        chaine = s1[0:coupe]
    else:
        coupe = (len(s1)+1)//2
        chaine = '1' + (coupe - 1) * '0'
    while(int(chaine+chaine) <= r2):
        if(int(chaine+chaine) >= r1):
            res += int(chaine+chaine)
        chaine = str(int(chaine)+1)
print(res)
# 53420042388

# Part 2

print('\n')
res = []
for plage in l:
    r = plage.split(sep='-')
    s1 = r[0]
    s2 = r[1]
    r1 = int(s1)
    r2 = int(s2)
    for k in range(2,len(s2)+1):
        if(len(s1) % k == 0):
            coupe = len(s1) // k
            chaine = s1[0:coupe]
        else:
            coupe = (len(s1)+1) // k
            chaine = '1' + (coupe - 1) * '0'
        valeur_testee = int(k * chaine)
        while(valeur_testee <= r2):
            if(valeur_testee >= r1):
                res.append(valeur_testee)
            chaine = str(int(chaine)+1)
            valeur_testee = int(k * chaine)

print(sum(set(res)))
# 69553832684