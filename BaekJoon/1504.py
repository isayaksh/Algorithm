# BOJ 1504 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

from sys import stdin, maxsize
from heapq import heappop, heappush
from collections import defaultdict

def solution(N, E, edges, u, v):
    
    # graph init
    graph = defaultdict(list)
    for a, b, c in edges:
        graph[a].append((b,c))
        graph[b].append((a,c))

    # dijkstra
    def dijkstra(u, v):
        result = [maxsize] * (N+1)
        result[u] = 0
        heap = [(0,u)]
        while heap:
            weight, node = heappop(heap)
            for nextNode, nextWeight in graph[node]:
                if result[nextNode] > weight + nextWeight:
                    result[nextNode] = weight + nextWeight
                    heappush(heap, (weight+nextWeight, nextNode))
        return result[v]
    
    # [case1] : 1 → u → v → N
    case1 = dijkstra(1,u) + dijkstra(u,v) + dijkstra(v,N)
    # [case2] : 1 → v → u → N
    case2 = dijkstra(1,v) + dijkstra(v,u) + dijkstra(u,N)

    return -1 if case1 >= maxsize and case2 >= maxsize else min(case1, case2)

N, E = map(int,stdin.readline().split())
edges = list(list(map(int,stdin.readline().split())) for _ in range(E))
u, v = map(int,stdin.readline().split())

result = solution(N, E, edges, u, v)
print(result)