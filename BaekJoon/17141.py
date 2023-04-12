# BOJ 17141 연구소 2
# https://www.acmicpc.net/problem/17141

from sys import stdin, maxsize
from itertools import combinations
from collections import deque

def solution(N, M, graph):
    answer = -1

    def check(visited):
        answer = 0
        for y in range(N):
            for x in range(N):
                if visited[y][x] == -1: return maxsize
                answer = max(answer, visited[y][x])
        return answer

    virus = [(x,y) for y in range(N) for x in range(N) if graph[y][x] == 2]
    wall = [(x,y) for y in range(N) for x in range(N) if graph[y][x] == 1]
    for y in range(N):
        for x in range(N):
            if graph[y][x] == 2: graph[y][x] = 0

    for case in combinations(virus, M):
        visited = [[-1] * N for _ in range(N)]
        for x, y in wall: visited[y][x] = 0
        for x, y in case: visited[y][x] = 0

        queue = deque(case)
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == -1 and graph[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx, ny))

        res = check(visited)
        if answer == -1 and res != maxsize:
            answer = res
        else:
            answer = min(answer, res)

    return answer

N, M = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

result = solution(N, M, graph)
print(result)