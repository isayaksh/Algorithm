# BOJ 1167 트리의 지름
# https://www.acmicpc.net/problem/1167

from sys import stdin
from collections import defaultdict, deque

def solution(V, edges):

    # 그래프 초기화
    graph = defaultdict(list)
    for edge in edges:
        for i in range(1, len(edge)-2, 2):
            graph[edge[0]].append(((edge[i], edge[i+1])))

    # BFS 탐색
    def bfs(startNode):
        visited = [-1] * (V + 1)
        visited[startNode] = 0
        queue = deque([startNode])
        while queue:
            node = queue.popleft()
            for nextNode, weight in graph[node]:
                if visited[nextNode] == -1:
                    visited[nextNode] = visited[node] + weight
                    queue.append(nextNode)

        maxWeight = max(visited)
        endNode = visited.index(maxWeight)
        return maxWeight, endNode
    
    # 1. 임의의 정점 x에서 가장 먼 정점 y를 찾는다.
    maxWeight, y = bfs(1)
    # 2. 정점 y에서 가장 먼 정점 z를 찾는다.
    maxWeight, z = bfs(y)

    return maxWeight

# input
V = int(stdin.readline())
edges = list(list(map(int,stdin.readline().split())) for _ in range(V))

# response
response = solution(V, edges)
print(response)