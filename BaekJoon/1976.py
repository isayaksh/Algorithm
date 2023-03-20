# BOJ 1976 여행 가자
# https://www.acmicpc.net/problem/1976

from sys import stdin

def solution(N, M, graph, order):
    # UNION & FIND
    parent = [i for i in range(N+1)]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        parent[max(x,y)] = min(x,y)

    # UNION
    edges = [(x,y) for y in range(N) for x in range(y+1,N) if graph[y][x] == 1]
    for x, y in edges:
        union(x, y)
    
    # FIND
    order = [o-1 for o in order]
    for i in range(M-1):
        if find(order[i]) != find(order[i+1]):
            return 'NO'
    return 'YES'

N = int(stdin.readline())
M = int(stdin.readline())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))
order = list(map(int,stdin.readline().split()))

result = solution(N, M, graph, order)
print(result)