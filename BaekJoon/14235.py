# 14235 크리스마스 선물 < 실버 3 >
import heapq
from sys import stdin
n = int(stdin.readline())
A = []
for _ in range(n):
  a = list(map(int,stdin.readline().split()))
  if a[0] == 0:
    if not A:
      print(-1)
    else:
      print(abs(heapq.heappop(A)))
  else:
    for i in range(a[0]):
      heapq.heappush(A,-a[i+1])