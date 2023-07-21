# BOJ 3187 양치기 꿍
# https://www.acmicpc.net/problem/3187

from sys import stdin

def solution(R, C, graph):
    sheep, woolf = 0, 0

    def dfs(x, y):
        fenceSheep, fenceWoolf = 0, 0
        
        if graph[y][x] == 'k': fenceSheep = 1
        if graph[y][x] == 'v': fenceWoolf = 1
        graph[y][x] = '#'

        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] != '#':
                    if graph[ny][nx] == 'k': fenceSheep += 1
                    if graph[ny][nx] == 'v': fenceWoolf += 1
                    graph[ny][nx] = '#'
                    stack.append((nx, ny))

        return (fenceSheep, 0) if fenceSheep > fenceWoolf else (0, fenceWoolf)
        
    for y in range(R):
        for x in range(C):
            if graph[y][x] != '#':
                fenceSheep, fenceWoolf = dfs(x, y)
                sheep, woolf = sheep + fenceSheep, woolf + fenceWoolf
    
    return sheep, woolf

R, C = map(int,stdin.readline().split())
graph = list(list(stdin.readline().strip()) for _ in range(R))

sheep, woolf = solution(R, C, graph)
print(sheep, woolf)