# 이친수

from sys import stdin

A = [[0,1]]

for i in range(90):
  A.append([A[i][0]+A[i][1],A[i][0]])

N = int(stdin.readline())
print(sum(A[N-1]))