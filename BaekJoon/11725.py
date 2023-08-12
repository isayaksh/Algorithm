# BOJ 11725 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6)

def solution(N, edges):

    answer = [0] * (N+1)

    # init graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(parent):
        for child in graph[parent]:
            if not answer[child]:
                answer[child] = parent
                dfs(child)
    
    dfs(1)

    print('\n'.join(map(str, [answer[i] for i in range(2, N+1)])))

N = int(stdin.readline())
edges = list(list(map(int,stdin.readline().split())) for _ in range(N-1))

solution(N, edges)