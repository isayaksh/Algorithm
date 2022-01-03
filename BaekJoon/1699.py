# 제곱수의 합

from sys import stdin
from math import sqrt

N = int(stdin.readline())

A = [0 for i in range(N+1)]
S = [i**2 for i in range(1,317)]

for i in range(1,N+1):
  r = []
  for j in S:
    if j > i:
      break
    r.append(A[i-j])
  A[i] = min(r)+1
print(A[N])