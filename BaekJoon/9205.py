# BOJ 9205 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

from sys import stdin
from collections import deque

def solution(n, sx, sy, convenienceStore, ex, ey):
    visited = [False] * n
    queue = deque([(sx, sy)])

    def checkDistance(sx, sy, ex, ey):
        return abs(sx-ex) + abs(sy-ey) <= 1000

    while queue:
        x, y = queue.popleft()
        if checkDistance(x, y, ex, ey):
            return 'happy'
        for i in range(n):
            if not visited[i]:
                nx, ny = convenienceStore[i]
                if checkDistance(x, y, nx, ny):
                    visited[i] = True
                    queue.append((nx, ny))
    return 'sad'

t = int(stdin.readline())
for _ in range(t):
    answer = False
    # input
    n = int(stdin.readline())
    sx, sy = map(int,stdin.readline().split())
    convenienceStore = list(list(map(int,stdin.readline().split())) for _ in range(n))
    ex, ey = map(int,stdin.readline().split())
    # result
    result = solution(n, sx, sy, convenienceStore, ex, ey)
    print(result)