# 2*n 타일링

from sys import stdin

n = int(stdin.readline())

table = [0,1,2]
for i in range(3,n+1):
  table.append(table[i-1]+table[i-2])
print(table[n]%10007)