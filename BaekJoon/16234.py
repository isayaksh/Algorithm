# BOJ 16234 인구 이동
# https://www.acmicpc.net/problem/16234

from sys import stdin
from collections import deque

def solution(N, L, R, graph):
    answer = 0

    def partition():
        parts = []
        visited = [[False] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    part = [(x, y)]
                    # BFS
                    queue = deque([(x, y)])
                    visited[y][x] = True
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                            nx, ny = x + dx, y + dy
                            if (0 <= nx < N) and (0 <= ny < N) and not visited[ny][nx]:
                                if L <= abs(graph[ny][nx] - graph[y][x]) <= R:
                                    visited[ny][nx] = True
                                    part.append((nx, ny))
                                    queue.append((nx, ny))
                    if len(part) > 1:
                        parts.append(part)
        return parts
    
    def immigrant(part):
        population = sum([graph[y][x] for x, y in part]) // len(part)
        for x, y in part:
            graph[y][x] = population

    while True:
        parts = partition()
        if len(parts) == 0: break
        for part in parts:
            immigrant(part)
        answer += 1

    return answer

# input
N, L, R = map(int,stdin.readline().split())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

# response
response = solution(N, L, R, graph)
print(response)