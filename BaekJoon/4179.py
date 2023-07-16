# BOJ 4179 불!
# https://www.acmicpc.net/problem/4179

from sys import stdin
from collections import deque

def solution(R, C, graph):

    # 불 번짐
    def wildfire(fires):
        newFires = []
        for x, y in fires:
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == '.':
                    graph[ny][nx] = 'F'
                    newFires.append((nx, ny))
        return newFires
    
    # 지훈이의 위치
    for y in range(R):
        for x in range(C):
            if graph[y][x] == 'J':
                jx, jy = x, y
                graph[y][x] = '.'

    # 불의 위치
    fires = set([(x, y) for y in range(R) for x in range(C) if graph[y][x] == 'F'])

    # DFS
    minute = 1
    visited = [[False] * C for _ in range(R)]
    visited[jy][jx] = True
    queue = deque([(jx, jy, 1)])
    while queue:
        x, y, m = queue.popleft()
        
        # 
        if minute != m:
            fires = wildfire(fires)
            minute = m
        
        if graph[y][x] == 'F':
            continue

        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= C or ny < 0 or ny >= R:
                return m;
            if graph[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, m+1))

    return "IMPOSSIBLE"

# R, C = 4, 4
# graph = [['#', '#', '#', '#'], ['#', 'J', 'F', '#'], ['#', '.', '.', '#'], ['#', '.', '.', '#']]

R, C = map(int,stdin.readline().split())
graph = list(list(stdin.readline().strip()) for _ in range(R))

res = solution(R, C, graph)
print(res)