# BOJ 1707 이분 그래프
# https://www.acmicpc.net/problem/1707

from sys import stdin
from collections import defaultdict, deque

# BFS 탐색
def bfs(startNode):
    queue = deque([startNode])
    visited[startNode] = 1
    while queue:
        node = queue.popleft()
        for nextNode in graph[node]:
            if not visited[nextNode]:
                visited[nextNode] = -1 * visited[node]
                queue.append(nextNode)
            elif visited[nextNode] == visited[node]:
                return False
    return True

# MAIN
K = int(stdin.readline())
for _ in range(K):
    #input
    V, E = map(int,stdin.readline().split())
    edges = [list(map(int,stdin.readline().split())) for _ in range(E)]

    # 그래프 초기화
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (V+1)
    for node in range(1, V+1):
        if not visited[node]:
            flag = bfs(node)
            if not flag:
                break

    print("YES" if flag else "NO")