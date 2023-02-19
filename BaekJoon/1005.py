# BOJ 1005 ACM Craft
# https://www.acmicpc.net/problem/1005

from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush

def solution(N, K, D, XY, W):

    # 최소 건설 시간
    constructionTime = [0] * (N+1)

    # 진입 차수, 연결 관계 초기화
    indegree = [0] * (N+1)
    graph = defaultdict(list)
    for X, Y in XY:
        indegree[Y] += 1
        graph[X].append(Y)

    # 진입 차수가 없는 건물
    heap = [(D[i], i) for i in range(1, N+1) if indegree[i] == 0]

    # 위상 정렬
    while heap:
        time, node = heappop(heap)
        constructionTime[node] = time
        for nextNode in graph[node]:
            indegree[nextNode] -= 1
            if indegree[nextNode] == 0:
                heappush(heap,(time + D[nextNode], nextNode))

    return constructionTime[W]

T = int(stdin.readline())

for _ in range(T):
    N, K = map(int,stdin.readline().split())
    D = [0] + list(map(int,stdin.readline().split()))
    XY = list(list(map(int,stdin.readline().split())) for _ in range(K))
    W = int(stdin.readline())

    result = solution(N, K, D, XY, W)
    print(result)