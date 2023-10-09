# BOJ 16562 친구비
# https://www.acmicpc.net/problem/16562

from sys import stdin

def solution(N, M, K, A, relation):
    
    # union & find
    parent = [i for i in range(N+1)]
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        parent[max(x, y)] = min(x, y)

    # union
    for w, v in relation:
        union(w, v)

    # 최소 친구 비용
    cost = dict()    
    for i in range(1, N+1):
        j = find(i)
        if j in cost:
            cost[j] = min(cost[j], A[i-1])
        if j not in cost:
            cost[j] = A[i-1]
    
    totalCost = sum(cost.values())
    
    return totalCost if totalCost <= K else "Oh no"

# input
N, M, K = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
relation = list(list(map(int,stdin.readline().split())) for _ in range(M))

# result
res = solution(N, M, K, A, relation)
print(res)