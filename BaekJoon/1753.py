# BOJ 1753 최단경로
# https://www.acmicpc.net/problem/1753

from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

def solution(V, K, edges):
    
    answer = [maxsize] * (V+1)
    answer[K] = 0

    # graph init
    graph = defaultdict(list)
    for s, e, w in edges:
        graph[s].append((w,e))
    
    # dijkstra
    heap = [(0, K)]
    while heap:
        weight, node = heappop(heap)

        for nextWeight, nextNode in graph[node]:
            if answer[nextNode] > nextWeight + weight:
                answer[nextNode] = nextWeight + weight
                heappush(heap, (nextWeight + weight, nextNode))

    return answer[1:]

# input
V, E = map(int,stdin.readline().split())
K = int(stdin.readline())
edges = [map(int,stdin.readline().split()) for _ in range(E)]

# result
result = solution(V, K, edges)
for res in result:
    print(res if res != maxsize else 'INF')