# BOJ 13308 주유소
# https://www.acmicpc.net/problem/13308

from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

def solution(N, M, gas, edges):

    graph = defaultdict(list)
    for s, e, w in edges:
        graph[s].append((e,w))
        graph[e].append((s,w))
    
    cost = [[maxsize] * (N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        cost[i][i] = 0

    heap = [(0, gas[1], 1)]
    while heap:
        currentCost, minGas, node = heappop(heap)

        if node == N:
            return currentCost

        for nextNode, weight in graph[node]:
            newCost = minGas * weight
            if cost[node][nextNode] > newCost:
                cost[node][nextNode] = newCost
                heappush(heap,(currentCost + newCost, min(minGas, gas[nextNode]), nextNode))

N, M = map(int,stdin.readline().split())
gas = [-1] + list(map(int,stdin.readline().split()))
edges = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, gas, edges)
print(res)