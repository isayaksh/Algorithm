# 1374 강의실 <골드 5>
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline())
lectures = []
for _ in range(N):
    num, start, end = map(int,stdin.readline().split())
    lectures.append((start,end))
lectures.sort() # 강의 시작 시간을 기준으로 오름차순으로 정렬
H = [lectures[0][1]] # 힙에 가장빨리 시작하는 강의의 종료 시간을 추가
for i in range(1,N):
    start, end = lectures[i]
    # 힙에 있는 강의 중 가장 빨리 끝나는 강의 시간 pop()
    hEnd = heappop(H) 
    # 현재 강의의 시작 시간보다 힙에 있는 강의 중 가장 빨리 끝나는 강의 시간이 크다면
    # pop() 한 끝나는 강의 시간을 다시 push()
    if start < hEnd: heappush(H,hEnd) 
    # 현재 강의의 끝나는 시간 힙에 push()
    heappush(H,end) 
print(len(H))