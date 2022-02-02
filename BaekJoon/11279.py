# 11279 최대 힙 <실버 2>
import heapq
from sys import stdin

N = int(stdin.readline())

H = []

for _ in range(N):
  num = int(stdin.readline())
  if num:
    heapq.heappush(H,-num)
  else:
    if not H:
      print(0)
    else:
      print(abs(heapq.heappop(H)))