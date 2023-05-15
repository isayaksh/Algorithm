# BOJ 4485 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

from sys import stdin, maxsize
from collections import deque

def solution(N, graph):
    minGraph = [[maxsize] * N for _ in range(N)]
    minGraph[0][0] = graph[0][0]
    
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and minGraph[y][x] + graph[ny][nx] < minGraph[ny][nx]:
                minGraph[ny][nx] = minGraph[y][x] + graph[ny][nx]
                queue.append((nx, ny))

    return minGraph[-1][-1]

for i in range(1, maxsize):
    N = int(stdin.readline())
    if N == 0: break
    graph = list(list(map(int,stdin.readline().split())) for _ in range(N))
    print(f'Problem {i}: {solution(N, graph)}')