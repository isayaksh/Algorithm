# BOJ 2194 유닛 이동시키기
# https://www.acmicpc.net/problem/2194

from sys import stdin
from collections import deque

def solution(N, M, A, B, K, hurdle, Sy, Sx, Ey, Ex):

    def checkBox(x, y):
        for dy in range(A):
            for dx in range(B):
                nx, ny = x + dx, y + dy
                if (ny, nx) in hurdle:
                    return False
                if nx < 1 or nx > M or ny < 1 or ny > N:
                    return False
        return True

    # BFS
    visited = [[False] * (M+1) for _ in range(N+1)]
    queue = deque([(Sx, Sy, 0)])
    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == (Ex, Ey):
            return cnt

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 < nx <= M and 0 < ny <= N and not visited[ny][nx] and checkBox(nx, ny):
                visited[ny][nx] = True
                queue.append((nx ,ny, cnt+1))
    
    return -1

N, M, A, B, K = map(int,stdin.readline().split())
hurdle = set(tuple(map(int,stdin.readline().split())) for _ in range(K))
Sy, Sx = map(int,stdin.readline().split())
Ey, Ex = map(int,stdin.readline().split())

res = solution(N, M, A, B, K, hurdle, Sy, Sx, Ey, Ex)
print(res)