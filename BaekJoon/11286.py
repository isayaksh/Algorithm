# 11286 절대값 힙 < 실버 1>
from sys import stdin
import heapq

N = int(stdin.readline())
H = [] # 힙
for _ in range(N):
  x = int(stdin.readline())
  if x: # 만약 x가 0이 아닌 정수 값이라면
    heapq.heappush(H,[abs(x),x]) # 힙에 x 추가
  else: # x가 0이고
    if not H: # 힙이 비어있다면
      print(0) # 0 출력
    else: # 힙에 원소가 있다면
      print(heapq.heappop(H)[1]) # 제일 작은 원소 출력