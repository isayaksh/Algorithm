# 1927 최소 힙 <실버 2>
from sys import stdin
import heapq
N = int(stdin.readline())
H = []
for _ in range(N):
  x = int(stdin.readline())
  if x:
    heapq.heappush(H,x)
  else:
    if not H:
      print(0)
    else:
      print(heapq.heappop(H))