# BOJ 17144 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

from sys import stdin
from collections import deque

def solution(R, C, T, graph):

    # 위쪽 공기청정기, 아래쪽 공기청정기
    (top, bottom) = [y for y in range(R) if graph[y][0] == -1]

    def airPurifierWorking():
        # 공기청정기로 들어간 미세먼지는 모두 정화
        graph[top-1][0], graph[bottom+1][0] = 0, 0

        # 위쪽 공기청정기
        for y in range(top-1, -1, -1):
            graph[y+1][0] = graph[y][0]
        graph[0].popleft()    
        graph[0].append(0)
        for y in range(1, top+1):
            graph[y-1][-1] = graph[y][-1]
        graph[top].pop()
        graph[top].appendleft(-1)

        # 아래쪽 공기청정기
        for y in range(bottom+1, R):
            graph[y-1][0] = graph[y][0]
        graph[-1].popleft()    
        graph[-1].append(0)
        for y in range(R-2, bottom-1, -1):
            graph[y+1][-1] = graph[y][-1]
        graph[bottom].pop()
        graph[bottom].appendleft(-1)
    
    def spreadFineDust():
        spreadGraph = [[0] * C for _ in range(R)]

        # 확산 가능한 미세먼지
        fineDust = [(x, y) for y in range(R) for x in range(C) if graph[y][x] >= 5]
        for x, y in fineDust:
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny, dust = x + dx, y + dy, graph[y][x]//5
                if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] != -1:
                    spreadGraph[ny][nx] += dust
                    spreadGraph[y][x] -= dust
        
        # 미세먼지 갱신
        for y in range(R):
            for x in range(C):
                graph[y][x] += spreadGraph[y][x]
        
    for _ in range(T):
        spreadFineDust()
        airPurifierWorking()

    return sum(map(sum,graph)) + 2

R, C, T = map(int,stdin.readline().split())
graph = [deque(map(int,stdin.readline().split())) for _ in range(R)]

result = solution(R, C, T, graph)
print(result)