# 1, 2, 3 더하기

from sys import stdin

T = int(stdin.readline())

inp = [int(stdin.readline()) for _ in range(T)]

M = max(inp)
A=[0,1,2,4]

for i in range(4,M+1):
  A.append(A[i-1]+A[i-2]+A[i-3])
for i in inp:
  print(A[i])