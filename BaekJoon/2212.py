# 2212 센서 < 골드 5 >
import heapq
from sys import stdin
N = int(stdin.readline()) # 센서의 개수
K = int(stdin.readline()) # 집중국의 개수
M = sorted(list(map(int,stdin.readline().split()))) # 센서 위치 오름차순 정렬
if N < K: # 센서보다 집중국의 개수가 많으면
  print(0)
  exit()
distance = [] # 센서 간 거리 값
for i in range(N-1):
  heapq.heappush(distance, M[i] - M[i+1])
for _ in range(K-1):
  heapq.heappop(distance)
print(abs(sum(distance)))