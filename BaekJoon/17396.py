# BOJ 17396 백도어
# https://www.acmicpc.net/problem/17396

from sys import stdin, maxsize
from heapq import heappop, heappush
from collections import defaultdict

def solution(N, M, sight, edges):
    
    # minimum time
    time = [maxsize] * N
    time[0] = 0

    # is it in sight?
    sight[-1] = 0
    inSight = [True if sight[i] == 0 else False for i in range(N)]

    # init graph
    graph = defaultdict(list)
    for u, v, w in edges:
        if inSight[u] and inSight[v]:
            graph[u].append([v, w])
            graph[v].append([u, w])
    
    # dijkstra
    heap = [(0, 0)]
    while heap:
        weight, node = heappop(heap)
        if weight > time[node]:
            continue
        for nextNode, nextWeight in graph[node]:
            if time[nextNode] > weight + nextWeight:
                time[nextNode] = weight + nextWeight
                heappush(heap, (weight + nextWeight, nextNode))
    
    return time[-1] if time[-1] != maxsize else -1

N, M = map(int,stdin.readline().split())
sight = list(map(int,stdin.readline().split()))
edges = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, sight, edges)
print(res)