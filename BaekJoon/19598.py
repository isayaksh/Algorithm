# 19598 최소 회의실 개수 < 골드 5 >
import heapq
from sys import stdin
conf = [] # 강의, 우선순위큐
count = 1 # 강의실 개수

N = int(stdin.readline())
for _ in range(N):
  conf.append(list(map(int,stdin.readline().split())))
conf.sort() # 오름차순으로 정렬
heap = [conf[0][1]]

for i in range(1,N):
  if heap[0] <= conf[i][0]: # 현재 강의실 중 가장 빨리 끝나는 강의실 <= 현재 수업의 시작 시간
    heapq.heappop(heap) #  현재 강의실 중 가장 빨리 끝나는 강의실 제거
  else: # 현재 강의실 중 가장 빨리 끝나는 강의실 > 현재 수업의 시작 시간
    count+=1 # 강의실 1개 추가
  heapq.heappush(heap,conf[i][1]) # 현재 수업 종료 시간 추가
print(count)