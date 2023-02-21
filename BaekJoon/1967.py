# BOJ 1967 트리의 지름
# https://www.acmicpc.net/problem/1967

from sys import stdin, maxsize
from heapq import heappop, heappush

def solution(n, edges):

    graph = [[] for _ in range(n+1)]
    for s, e, w in edges:
        graph[s].append((w, e))
        graph[e].append((w, s))
    
    def bfs(start):
        weights = [maxsize] * (n+1)
        weights[start] = 0
        heap = [(0, start)]
        while heap:
            weight, node = heappop(heap)
            for w, e in graph[node]:
                if weights[e] > weight + w:
                    weights[e] = weight + w
                    heappush(heap, (weight + w, e))
        maxWeight = max(weights[1:])
        return weights.index(maxWeight), maxWeight
    
    idx1, weight1 = bfs(1)
    idx2, weight2 = bfs(idx1)

    return weight2

# input
n = int(stdin.readline())
edges = [list(map(int,stdin.readline().split())) for _ in range(n-1)]

# result
result = solution(n, edges)
print(result)