# 합분해

from sys import stdin
import time

N,K = map(int,stdin.readline().split())

A = [[0 for _ in range(201)] for _ in range(201)]

for i in range(201):
  A[1][i] = 1
  A[2][i] = i+1
  A[i][1] = i

for i in range(2,201):
  for j in range(2,201):
    A[i][j] = (A[i-1][j] + A[i][j-1]) % 1000000000
print(A[K][N])