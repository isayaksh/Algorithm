# BOJ 17070 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070

from sys import stdin

def dfs(x, y, t):
    global answer
    # 도착
    if (x, y) == (N-1, N-1):
        answer += 1
        return
    # 대각선(↘)
    if x + 1 < N and y + 1 < N and graph[y][x+1] == 0 and graph[y+1][x] == 0 and graph[y+1][x+1] == 0:
        dfs(x+1, y+1, 2)
    # 가로(→)
    if t != 1 and x + 1 < N and graph[y][x+1] == 0 :
        dfs(x+1, y, 0)
    # 세로(↓)
    if t != 0 and y + 1 < N and graph[y+1][x] == 0:
        dfs(x, y+1, 1)
    
N = int(stdin.readline())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

answer = 0
dfs(1, 0, 0)
print(answer)