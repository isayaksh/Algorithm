# BOJ 18405 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from sys import stdin
from collections import deque

def solution(N, K, graph, S, X, Y):
    # 초기 바이러스 위치 찾기
    queue = deque(sorted([[x, y, graph[y][x], 0] for y in range(N) for x in range(N) if graph[y][x] != 0], key=lambda x : x[2]))

    # BFS
    while queue:
        x, y, value, time = queue.popleft()
        if time >= S: break
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == 0:
                graph[ny][nx] = value                
                queue.append([nx, ny, value, time+1])
    return graph[X-1][Y-1]

# input
N, K = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))
S, X, Y = map(int,stdin.readline().split())

# result
res = solution(N, K, graph, S, X, Y)
print(res)