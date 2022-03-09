# 2075 N번째 큰 수 < 골드 5 >
import heapq
from sys import stdin
N = int(stdin.readline())
Heap = list(map(int,stdin.readline().split()))
heapq.heapify(Heap) # 힙 구조
for _ in range(N-1):
  Values = map(int,stdin.readline().split())
  for value in Values:
    if  Heap[0] < value:
      heapq.heappop(Heap) # 힙의 최소값을 제거
      heapq.heappush(Heap,value) # 힙에 최소값보다 큰 값을 추가
print(Heap[0])