# BOJ 15900 나무 탈출
# https://www.acmicpc.net/problem/15900

from sys import stdin
from collections import defaultdict

def solution(N, edges):

    # create tree
    tree = defaultdict(list)
    for node1, node2 in edges:
        tree[node1].append(node2)
        tree[node2].append(node1)

    # bfs
    distance = [0] * (N+1)
    distance[1] = 1

    stack = [(1, 0)]
    while stack:
        node, count = stack.pop()
        for nextNode in tree[node]:
            if distance[nextNode] == 0:
                distance[nextNode] = count + 1
                stack.append((nextNode, count+1))
    
    return "Yes" if sum([distance[i] for i in range(2, N+1) if len(tree[i]) == 1])%2 else "No"

N = int(stdin.readline())
edges = list(list(map(int,stdin.readline().split())) for _ in range(N-1))

res = solution(N, edges)
print(res)