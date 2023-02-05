# BOJ 1261 알고스팟
# https://www.acmicpc.net/problem/1261

from sys import stdin
from collections import deque

def solution(N, M, graph):

    # 벽을 부순 횟수
    count = [[10001] * (N) for _ in range(M)]
    count[0][0] = 0
    queue = deque([(0, 0)])

    # bfs
    while queue:
        x, y = queue.popleft()
        # 도착
        if x == N-1 and y == M-1:
            continue
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if (0 <= nx < N) and (0 <= ny < M):
                if graph[ny][nx] == '1':
                    if count[ny][nx] > count[y][x] + 1:
                        count[ny][nx] = count[y][x] + 1
                        queue.append((nx ,ny))
                else:
                    if count[ny][nx] > count[y][x]:
                        count[ny][nx] = count[y][x]
                        queue.append((nx, ny))
    return count[M-1][N-1]

N, M = map(int,stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(M)]

res = solution(N, M, graph)
print(res)