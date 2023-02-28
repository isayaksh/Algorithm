# BOJ 3055 탈출
# https://www.acmicpc.net/problem/3055

from sys import stdin, maxsize
from collections import deque

def solution(R, C, graph):

    distance = [[maxsize] * C for _ in range(R)]

    queue = deque()
    
    for y in range(R):
        for x in range(C):
            if graph[y][x] == 'S':
                queue.append((x,y))
                distance[y][x] = 0
            if graph[y][x] == 'D':
                Dx, Dy = x, y
    
    for y in range(R):
        for x in range(C):
            if graph[y][x] == '*':
                queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        if distance[Dy][Dx] != maxsize:
            return distance[Dy][Dx]
        
        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < C and 0 <= ny < R:
                if graph[y][x] == 'S' and (graph[ny][nx] == '.' or graph[ny][nx] == 'D'):
                    if distance[ny][nx] > distance[y][x] + 1:
                        distance[ny][nx] = distance[y][x] + 1
                        graph[ny][nx] = 'S'
                        queue.append((nx,ny))

                if graph[y][x] == '*' and (graph[ny][nx] == '.' or graph[ny][nx] == 'S'):
                    graph[ny][nx] = '*'
                    queue.append((nx,ny))

    return "KAKTUS"

R, C = map(int,stdin.readline().split())
graph = list(list(stdin.readline().strip()) for _ in range(R))

result = solution(R, C, graph)
print(result)