# 골드바흐 파티션

from sys import stdin
from math import sqrt

T = int(stdin.readline())
N = [int(stdin.readline()) for _ in range(T)]
# 입력값을 한번에 받아서 가장 큰 값을 이용하여 중복을 방지!
Max = max(N) 

A = [True]*(Max+1)

for i in range(2,int(sqrt(Max))+1):
  if A[i]:
    for j in range(2*i, Max+1, i):
      if A[j]:
        A[j] = False

for n in N:
  count = 0
  for i in range(2,(n//2)+1):
    if A[i] and A[n-i]:
      count+=1
  print(count)

