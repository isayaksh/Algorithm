# BOJ 1238 파티
# https://www.acmicpc.net/problem/1238

from sys import stdin, maxsize
from heapq import heappop, heappush
from collections import defaultdict

def solution1(N, X, edges):
    answer = 0

    # 마을 간 이동 시간 list → defaultdict
    graph = defaultdict(list)
    for s, e, w in edges:
        graph[s].append((e,w))

    # X → I 이동 최단 시간
    def createXToIGraph():
        xToIGraph = [maxsize] * (N+1)
        xToIGraph[X] = 0
        heap = [(0,X)]
        while heap:
            w, node = heappop(heap)
            for nextNode, weight in graph[node]:
                if xToIGraph[nextNode] > w + weight:
                    xToIGraph[nextNode] = w + weight
                    heappush(heap, (w+weight, nextNode))
        return xToIGraph
    
    # I → X 이동 최단 시간
    def findMinIToX(i):
        itoXGraph = [maxsize] * (N+1)
        itoXGraph[i] = 0
        heap = [(0,i)]
        while heap:
            w, node = heappop(heap)
            if node == X: continue
            for nextNode, weight in graph[node]:
                if itoXGraph[nextNode] > w + weight:
                    itoXGraph[nextNode] = w + weight
                    heappush(heap, (w+weight, nextNode))
        
        return itoXGraph[X]

    xToIGraph = createXToIGraph()
    
    for i in range(1, N+1):
        if i == X: continue
        # (X → I → X) 최장 시간 갱신
        answer = max(answer, xToIGraph[i] + findMinIToX(i)) 

    return answer

# input
N, M, X = map(int,stdin.readline().split())
edges = [list(map(int,stdin.readline().split())) for _ in range(M)]

# response
res = solution1(N, X, edges)
print(res)