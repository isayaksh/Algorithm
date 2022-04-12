# 1781 컵라면 < 골드 3 >
import heapq
from sys import stdin
N = int(stdin.readline())
lst = []
result = []
for _ in range(N):
  deadline, ramen = map(int,stdin.readline().split())
  lst.append((deadline, ramen))
lst.sort()
for dr in lst:
  heapq.heappush(result,dr[1]) # 힙에 라면 갯수 추가
  if len(result) > dr[0]: # 만약 deadline 보다 현재 힙의 원소가 많다면
    heapq.heappop(result) # 힙의 원소 중 가장 작은 원소 제거
print(sum(result))