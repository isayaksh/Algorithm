# BOJ 13418 학교 탐방하기
# https://www.acmicpc.net/problem/13418

from sys import stdin
from collections import defaultdict

def solution(N, M, uphill, downhill):
    def getFatigue(hill):
        fatigue = 0
        parent = [i for i in range(N+1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            parent[max(x, y)] = min(x, y)               
        
        for node1, node2 in hill:
            node1, node2 = find(node1), find(node2)
            if node1 != node2:
                union(node1, node2)
                fatigue += 1
        return fatigue
    
    return getFatigue(uphill)**2 - (N - getFatigue(downhill))**2

N, M = map(int,stdin.readline().split())
uphill, downhill = [], []
for i in range(M+1):
    edges = list(map(int,stdin.readline().split()))
    uphill.append(edges[:2]) if edges[2] == 0 else downhill.append(edges[:2])

res = solution(N, M, uphill, downhill)
print(res)