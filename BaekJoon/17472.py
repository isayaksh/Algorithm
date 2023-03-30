# BOJ 17472 다리 만들기 2
# https://www.acmicpc.net/problem/17472

from sys import stdin, maxsize
from collections import defaultdict, deque

def solution(N, M, graph):
    answer = 0
    startPoint = defaultdict(list)
    def speDfs(x, y, count):
        startPoint[count].append((x,y))
        graph[y][x], visited[y][x] = count, True
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] and not visited[ny][nx]:
                speDfs(nx, ny, count)
    def conBfs(x, y, key):
        queue = deque([(x, y, dx, dy, 0) for dx, dy in ((1,0), (0,1), (-1,0), (0,-1))])
        while queue:
            x, y, dx, dy, cnt = queue.popleft()
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0:
                    queue.append((nx, ny, dx, dy, cnt+1))
                if graph[ny][nx] != 0 and graph[ny][nx] != key and cnt > 1:
                    result[key][graph[ny][nx]] = min(result[key][graph[ny][nx]], cnt)
                    result[graph[ny][nx]][key] = min(result[graph[ny][nx]][key], cnt)
    # UNION & FIND
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        parent[max(x,y)] = min(x,y)
    # 섬 구분
    visited = [[False] * M for _ in range(N)]
    count = 1
    for y in range(N):
        for x in range(M):
            if graph[y][x] and not visited[y][x]:
                speDfs(x, y, count)
                count += 1
    # 최소 연결 다리 찾기
    result = [[maxsize] * (count) for _ in range(count)]
    for key, values in startPoint.items():
        for x, y in values:
            conBfs(x, y, key)
    # 다리 연결
    edges = [(x, y, result[y][x]) for y in range(1,count) for x in range(y+1, count) if result[y][x] != maxsize]
    edges.sort(key=lambda x : x[2])
    parent = [i for i in range(count)]
    for x, y, v in edges:
        x, y = find(x), find(y)
        if x != y:
            union(x, y)
            answer += v
    # 모든 다리 연결 검증
    for i in range(2, count):
        if find(1) != find(i):
            return -1

    return answer

N, M = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

result = solution(N, M, graph)
print(result)