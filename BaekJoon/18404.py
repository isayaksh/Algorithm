# BOJ 18404 현명한 나이트
# https://www.acmicpc.net/problem/18404

from sys import stdin, maxsize
from collections import deque

def solution(N, M, X, Y, oppositeHorse):
    
    dp = [[maxsize] * (N+1) for _ in range(N+1)]
    dp[Y][X] = 0

    queue = deque([(X, Y)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)):
            nx, ny = x + dx, y + dy
            if 0 < nx <= N and 0 < ny <= N and dp[y][x] + 1 < dp[ny][nx]:
                dp[ny][nx] = dp[y][x] + 1
                queue.append((nx, ny))

    return [dp[y][x] for y, x in oppositeHorse]

N, M = map(int,stdin.readline().split())
Y, X = map(int,stdin.readline().split())
oppositeHorse = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, X, Y, oppositeHorse)
print(*res)