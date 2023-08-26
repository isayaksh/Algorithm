# BOJ 17086 아기 상어2
# https://www.acmicpc.net/problem/17086

from sys import stdin, maxsize
from collections import deque

def solution(N, M, graph):
    answer = [[maxsize] * (M) for _ in range(N)]

    # init queue
    queue = deque()
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                answer[y][x] = 0
                queue.append((x, y))
    
    # bfs
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((0,-1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and answer[y][x] + 1 < answer[ny][nx]:
                answer[ny][nx] = answer[y][x] + 1
                queue.append((nx, ny))
    
    return max([max(ans) for ans in answer])

N, M = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, M, graph)
print(res)