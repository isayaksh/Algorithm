# BOJ 17484 진우의 달 여행 (Small)
# https://www.acmicpc.net/problem/17484

from sys import stdin

def solution(N, M, graph):
    answer = []
    dx = [-1, 0, 1]

    def dfs(x, y, way, fuel):
        fuel += graph[y][x]

        if y == N-1:
            answer.append(fuel)
            return
        
        for i in range(3):
            if i == way: continue
            nx = x + dx[i]
            if 0 <= nx < M:
                dfs(nx, y+1, i, fuel)
    
    for x in range(M):
        dfs(x, 0, -1, 0)

    return min(answer)
    
N, M = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, M, graph)
print(res)