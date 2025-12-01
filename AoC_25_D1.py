import os
os.chdir('C:/Users/MMAJR1/Documents/Perso/R for fun/AdventOfCode/AoC2025/')
d1 = open('D1.txt', 'r')

pos = 50
# part 1
res = 0
# part 1
res2 = 0

for ligne in d1:
   # print(ligne)
   dir = ligne[0]
   val = int(ligne[1:])
#   print(dir)
#   print(val)
   res2 += val // 100
   val = val % 100
#   while(val > 100):
#      val -= 100
#       res2 += 1
   if(dir == 'R'):
      if(pos + val > 99):
          res2 +=1
      pos += val 
      pos = pos % 100
   if(dir == 'L'):
      if(pos <= val and pos > 0):
          res2 +=1
      pos -= val 
      pos = pos % 100
   if(pos == 0):
       res += 1 

print(res)
# 1168
print(res2)
# 7199
