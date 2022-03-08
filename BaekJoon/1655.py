# 1655 가운데를 말해요 < 골드 2 >
import heapq
from sys import stdin

leftH = []
rightH  = []

N = int(stdin.readline())
for _ in range(N):
  num = int(stdin.readline())
  if len(leftH) == len(rightH):
    heapq.heappush(leftH, [-num ,num])
  else:
    heapq.heappush(rightH,[num, num])
  if rightH and leftH[0][1] > rightH[0][1]:
    tmp1 = heapq.heappop(leftH)[1]
    tmp2 = heapq.heappop(rightH)[1]
    heapq.heappush(leftH, [-tmp2, tmp2])
    heapq.heappush(rightH, [tmp1, tmp1])
  print(leftH[0][1])