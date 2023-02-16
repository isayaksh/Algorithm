# BOJ 1916 최소비용 구하기
# https://www.acmicpc.net/problem/1916

from sys import stdin, maxsize
from heapq import heappop, heappush
from collections import defaultdict

def solution(N, M, edges, A, B):
    
    # 경로 갱신
    graph = defaultdict(list)
    for s, e, w in edges:
        graph[s].append((e, w))
    
    # 다익스트라
    heap = [(0, A)]
    cost = [maxsize] * (N+1)
    cost[A] = 0
    while heap:
        weight, node = heappop(heap)

        if cost[node] < weight:
            continue

        for nextNode, nextWeight in graph[node]:
            if weight + nextWeight < cost[nextNode]:
                cost[nextNode] = weight + nextWeight
                heappush(heap, (weight+nextWeight, nextNode))
    return cost[B]

# input
N = int(stdin.readline())
M = int(stdin.readline())
edges = [list(map(int,stdin.readline().split())) for _ in range(M)]
A, B = map(int,stdin.readline().split())

# result
result = solution(N, M, edges, A, B)
print(result)