# BOJ 7511 소셜 네트워킹 어플리케이션
# https://www.acmicpc.net/problem/7511

from sys import stdin

def solutuion(n, k, edges, m, relations):

    # UNION & FIND
    parent = [i for i in range(n+1)]
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        parent[max(x, y)] = min(x, y)
    
    # 1. 연결
    for u, v in edges:
        union(u, v)
    
    # 2. 확인
    for u, v in relations:
        u, v = find(u), find(v)
        print(1) if u == v else print(0)

T = int(stdin.readline())

for seq in range(1, T+1):
    n = int(stdin.readline())
    k = int(stdin.readline())
    edges = list(list(map(int,stdin.readline().split())) for _ in range(k))
    m = int(stdin.readline())
    relations = list(list(map(int,stdin.readline().split())) for _ in range(m))
    print(f"Scenario {seq}:")
    solutuion(n, k, edges, m, relations)
    print()