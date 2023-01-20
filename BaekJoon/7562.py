# BOJ 7562 나이트의 이동
from sys import stdin, maxsize
from collections import deque

# 모든 이동
dxy = [ (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2) ]

def solution(l, x1, y1, x2, y2):
    # graph 초기화
    graph = [[maxsize] * l for _ in range(l)]
    graph[y1][x1] = 0

    # 그래프 탐색
    queue = deque([(x1, y1)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # 체스판을 벗어난 경우
            if nx < 0 or nx >= l or ny < 0 or ny >= l: continue
            # 최단 경로 갱신
            if graph[ny][nx] > graph[y][x] + 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

    return graph[y2][x2]

T = int(stdin.readline())
for _ in range(T):
    l = int(stdin.readline())
    x1, y1 = map(int,stdin.readline().split())
    x2, y2 = map(int,stdin.readline().split())
    result = solution(l, x1, y1, x2, y2)
    print(result)