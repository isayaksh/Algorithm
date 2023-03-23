# BOJ 1766 문제집
# https://www.acmicpc.net/problem/1766

from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict

def solution(N, M, edges):
    answer = []

    # 진입차수, 진입관계
    indgree = [0] * (N+1)
    graph = defaultdict(list)
    for A, B in edges:
        indgree[B] += 1
        graph[A].append(B)

    # 진입차수가 0인 문제
    heap = []
    for i in range(1, N+1):
        if indgree[i] == 0:
            heappush(heap, i)
    
    # 위상정렬
    while heap:
        node = heappop(heap)
        answer.append(node)
        for nextNode in graph[node]:
            indgree[nextNode] -= 1
            if indgree[nextNode] == 0:
                heappush(heap, nextNode)
    return answer

# input
N, M = map(int,stdin.readline().split())
edges = list(list(map(int,stdin.readline().split())) for _ in range(M))

# result
result = solution(N, M, edges)
print(*result)