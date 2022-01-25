# 13904 과제 <골드 3>
from sys import stdin

N = int(stdin.readline())
A = []
M = 0
day = 1

for _ in range(N):
  d, w = map(int, stdin.readline().split())
  if d > M:
    M = d
  A.append([d,w])
result = [False for _ in range(M+1)]

A.sort(key = lambda x : x[1])

for i in range(N-1,-1,-1):
  for j in range(A[i][0],0,-1):
    if result[j] == False:
      result[j] = A[i][1]
      break
print(sum(result))