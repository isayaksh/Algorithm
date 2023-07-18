# BOJ 18223 민준이와 마산 그리고 건우
# https://www.acmicpc.net/problem/18223

from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

def solution(V, E, P, edges):

    # 간선 초기화
    edgeList = defaultdict(list)
    for src, dest, weight in edges:
        edgeList[src].append([dest, weight])
        edgeList[dest].append([src, weight])

    # 다잌스트라
    def dijkstra(src, dest):
        weightList = [maxsize] * (V+1)
        weightList[src] = 0
        heap = [(0, src)]
        while heap:
            weight, node = heappop(heap)
            for nextNode, nextWeight in edgeList[node]:
                if weightList[nextNode] > weight + nextWeight:
                    weightList[nextNode] = weight + nextWeight
                    heappush(heap, (weight+nextWeight, nextNode))
        return weightList[dest]

    return "SAVE HIM" if dijkstra(1, P) + dijkstra(P, V) == dijkstra(1, V) else "GOOD BYE"

V, E, P = map(int,stdin.readline().split())
edges = list(list(map(int,stdin.readline().split())) for _ in range(E))

res = solution(V, E, P, edges)
print(res)