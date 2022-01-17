# 15903 카드 합체 놀이
from sys import stdin
import heapq

n ,m = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
A.sort()
for i in range(m):
  Sum = heapq.heappop(A) + heapq.heappop(A)
  heapq.heappush(A,Sum)
  heapq.heappush(A,Sum)
print(sum(A))