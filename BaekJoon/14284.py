# BOJ 14284 간선 이어가기 2
# https://www.acmicpc.net/problem/14284

from sys import stdin, maxsize
from collections import defaultdict, deque

def solution(n, m, edges, s, t):

    # edges → edgesDictionary
    edgesDictionary = defaultdict(list)
    for firstNode, secondNode, weight in edges:
        edgesDictionary[firstNode].append((secondNode, weight))
        edgesDictionary[secondNode].append((firstNode, weight))
    
    # dijkstra
    sumOfWeight = [maxsize] * 5001
    sumOfWeight[s] = 0
    queue = deque([(s)])
    while queue:
        currentNode = queue.popleft()
        for nextNode, nextWeight in edgesDictionary[currentNode]:
            if sumOfWeight[currentNode] + nextWeight < sumOfWeight[nextNode]:
                sumOfWeight[nextNode] = sumOfWeight[currentNode] + nextWeight
                queue.append((nextNode))
    
    return sumOfWeight[t]

# input
n, m = map(int,stdin.readline().split())
edges = list(list(map(int,stdin.readline().split())) for _ in range(m))
s, t = map(int,stdin.readline().split())

# result
res = solution(n, m, edges, s, t)
print(res)