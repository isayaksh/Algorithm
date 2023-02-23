# BOJ 14500 테트로미노
# https://www.acmicpc.net/problem/14500

from sys import stdin
from itertools import combinations

def dfs(x, y, count, value):
    global answer
    if answer > value + max_val * (4 - count):
        return
    if count == 4:
        answer = max(answer, value)
        return
    for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, count+1, value+paper[ny][nx])
            visited[ny][nx] = False

def specialCase(x, y):
    global answer
    for case in cases:
        value = paper[y][x]
        for dx, dy in case:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                break
            value += paper[ny][nx]
        answer = max(answer, value)
    
# input
N, M = map(int,stdin.readline().split()) # 세로, 가로
paper = [list(map(int,stdin.readline().split())) for _ in range(N)]

# result
answer = 0
cases = list(combinations([(1,0), (0,1), (-1,0), (0,-1)], 3))
max_val = max(map(max, paper))

visited = [[False] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        specialCase(x, y)
        visited[y][x] = True
        dfs(x, y, 1, paper[y][x])
        visited[y][x] = False
print(answer)