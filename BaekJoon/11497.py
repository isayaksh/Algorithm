# 11497 통나무 건너뛰기 <실버1>
from sys import stdin
from collections import deque
T = int(stdin.readline())
for _ in range(T):
  N = int(stdin.readline())
  L = list(map(int,stdin.readline().split()))
  order = deque()
  L.sort()
  for i in range(N):
    if i%2:
      order.append(L[i])
    else:
      order.appendleft(L[i])
  result = abs(order[0]-order[-1])
  for i in range(N-1):
    if result < abs(order[i]-order[i+1]):
      result = abs(order[i]-order[i+1])
  print(result) 