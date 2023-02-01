# BOJ 1516 게임 개발
# https://www.acmicpc.net/problem/1516

from sys import stdin
from collections import deque, defaultdict

def solution(N, edges):

    pureCost = defaultdict(int) # 각 건물 순수 비용
    prerequisite = defaultdict(list) # 선수 건물 목록
    degree = [0] * (N+1) # 건물 진입 차수

    for i in range(N):
        pureCost[i+1] = edges[i][0] # 각 건물 순수 비용 갱신
        for edge in edges[i][1:-1]: 
            prerequisite[edge].append(i+1) # 선수 건물 목록 갱신
            degree[i+1] += 1 # 건물 진입 차수 갱신

    
    cost = [0] * (N+1) # 건물 짓는 비용
    queue = deque()
    for i in range(1, N+1):
        if degree[i] == 0: # 진입 차수가 없는 건물
            queue.append(i) # queue에 추가
            cost[i] = pureCost[i] # 건물 짓는 비용 갱신

    while queue:
        building = queue.popleft()
        # 건물(building)을 선수 건물로 하는 건물(b)
        for b in prerequisite[building]:
            degree[b] -= 1 # 진입 차수 -1
            cost[b] = max(cost[b], pureCost[b] + cost[building]) # 건물 건설에 걸리는 시간 갱신
            # 선수로 지어야 하는 건물이 존재하지 않을 경우
            if degree[b] == 0:
                queue.append(b)
    
    return cost[1:]

# input
N = int(stdin.readline())
edges = [list(map(int,stdin.readline().split())) for _ in range(N)]

# res
res = solution(N, edges)
for r in res: print(r)