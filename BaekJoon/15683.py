# BOJ 15683 감시
# https://www.acmicpc.net/problem/15683

from sys import stdin
from copy import deepcopy
from collections import deque

answer = 65

cases = [[],
         [[0], [1], [2], [3]],
         [[0,2], [1,3]],
         [[0,1], [1,2], [2,3], [3,0]],
         [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
         [[0,1,2,3]]]
direct = [(1,0), (0,1), (-1,0), (0,-1)]

def countZero(graph):
    return sum([g.count(0) for g in graph])

def dfs(graph, cctvs):

    if not cctvs:
        global answer
        answer = min(answer, countZero(graph))
        return
    
    type, x, y = cctvs[0]
    for case in cases[type]:
        newGraph = deepcopy(graph)
        queue = deque((x, y, direct[c][0], direct[c][1]) for c in case)

        while queue:
            (nx, ny, dx, dy) = queue.popleft()
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < M and 0 <= ny < N and newGraph[ny][nx] != 6:
                newGraph[ny][nx] = '#'
                queue.append((nx, ny, dx, dy))
        
        dfs(newGraph, cctvs[1:])


# input
N, M = map(int,stdin.readline().split())
graph = [list(map(int,stdin.readline().split())) for _ in range(N)]

# result
cctvs = [(graph[y][x], x, y) for x in range(M) for y in range(N) if 0 < graph[y][x] < 6]
dfs(graph, cctvs)
print(answer)