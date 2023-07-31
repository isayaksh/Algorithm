# BOJ 14716 현수막
# https://www.acmicpc.net/problem/14716

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def solution(M, N, banner):
    
    def dfs(x, y):
        visited[y][x] = True
        for dx, dy in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and banner[ny][nx]:
                dfs(nx, ny)
    
    answer = 0
    visited = [[False] * N for _ in range(M)]
    for y in range(M):
        for x in range(N):
            if not visited[y][x] and banner[y][x]:
                dfs(x, y)
                answer += 1
    
    return answer

M, N = map(int,stdin.readline().split())
banner = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(M, N, banner)
print(res)