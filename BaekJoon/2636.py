# BOJ 2636 치즈
# https://www.acmicpc.net/problem/2636

from sys import stdin
from collections import deque

def solution(R, C, graph):
    time, cheese = 0, 0

    def melt():
        visited = [[False] * C for _ in range(R)]
        visited[0][0] = True
        c = []

        queue = deque([(0,0)])
        while queue:
            x, y = queue.popleft()

            if graph[y][x] == 1:
                c.append((x,y))
                continue

            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx,ny))
        
        for x, y in c:
            graph[y][x] = 0

    while True:
        remainCheese = sum(map(sum,graph))
        if remainCheese == 0:
            break
        cheese = remainCheese
        time += 1

        melt()


    
    return time, cheese
        

R, C = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(R))

time, cheese = solution(R, C, graph)
print(time)
print(cheese)