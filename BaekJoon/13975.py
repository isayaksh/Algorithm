# 13975 파일 합치기 3 <골드 4>
from sys import stdin
import heapq
T = int(stdin.readline())

for _ in range(T):
  K = int(stdin.readline())
  F = list(map(int,stdin.readline().split()))
  F.sort()
  result = 0
  for _ in range(K-1):
    f = heapq.heappop(F) + heapq.heappop(F)
    result += f
    heapq.heappush(F,f)
  print(result)