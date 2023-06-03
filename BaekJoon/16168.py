# BOJ 16168 퍼레이드
# https://www.acmicpc.net/problem/16168

from sys import stdin

def solution(V, E, edges):
    # degree
    degree = [0] * (V+1)

    # UNION & FIND
    parents = [i for i in range(V+1)]
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        x, y = find(x), find(y)
        parents[max(x,y)] = min(x,y)

    for v1, v2 in edges:
        union(v1, v2)
        degree[v1] += 1
        degree[v2] += 1
    
    # 1개의 컴포넌트로 구성되어 있는지 확인
    pivot = find(1)
    for num in range(2, V+1):
        if pivot != find(num):
            return "NO"
    
    # 차수가 홀수인 정점의 수
    count = 0
    for num in range(1, V+1):
        if degree[num]%2:
            count += 1
    
    return "YES" if (count == 2 or count == 0) else "NO"

# input
V, E = map(int,stdin.readline().split())
edges = list(list(map(int,stdin.readline().split())) for _ in range(E))

# result
result = solution(V, E, edges)
print(result)