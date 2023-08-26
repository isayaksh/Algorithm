# BOJ 2211 네트워크 복구
# https://www.acmicpc.net/problem/2211

from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

def solution(N, M, circuit):
    parent = [0] * (N+1)
    
    # init graph
    graph = defaultdict(list)
    for node1, node2, weight in circuit:
        graph[node1].append((node2,weight))
        graph[node2].append((node1,weight))
    
    # DIJKSTRA
    weight = [0, 0] + [maxsize] * (N-1)
    heap = [(0, 1)]
    while heap:
        currentWeight, currentNode = heappop(heap)
        for nextNode, nextWeight in graph[currentNode]:
            newWeight = currentWeight + nextWeight
            if weight[nextNode] > newWeight:
                parent[nextNode] = currentNode
                weight[nextNode] = newWeight
                heappush(heap, (newWeight, nextNode))
    
    return [(i, parent[i]) for i in range(2, N+1)]

N, M = map(int,stdin.readline().split())
circuit = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, circuit)
print(N-1)
for node1, node2 in res:
    print(node1, node2)