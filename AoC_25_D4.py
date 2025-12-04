import os
import builtins

os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d4 = open('D4.txt', 'r')
# d4 = open('D4test.txt', 'r')

# data
df = d4.read()
m = df.split(sep='\n')
mat = []
for l in m:
    row=[]
    for k in l:
        row.append(k)
    if(row != []):
        mat.append(row)
n_row = len(mat)
n_col = len(mat[0])

# Fonction calculant le nb de voisins
def calc_nb_adj(mat):
    n_row = len(mat)
    n_col = len(mat[0])
    nb_adj = [[0 for _ in range(n_row + 2)] for _ in range(n_col + 2)]
    for i in range(n_row):
        for j in range(n_col):
            if(mat[i][j] == '@'):
                for k in range(3):
                    for l in range (3):
                        nb_adj[i+k][j+l] += 1
                nb_adj[i+1][j+1] -= 1
    return(nb_adj)

# Part 1
nb_adj = calc_nb_adj(mat)
res1 = 0
for i in range(n_row):
    for j in range(n_col):
        if(mat[i][j] == '@' and nb_adj[i+1][j+1] < 4):
            res1 += 1
print(res1)
# 1464

# Part 2
can_pick = True
res2 = 0
while(can_pick):
    nb_adj = calc_nb_adj(mat)
    res = 0
    for i in range(n_row):
        for j in range(n_col):
            if(mat[i][j] == '@' and nb_adj[i+1][j+1] < 4):
                res += 1
                mat[i][j] = '.'
    can_pick = (res > 0)
    res2 += res
print(res2)
# 8409