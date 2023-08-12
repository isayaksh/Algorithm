# BOJ 20955 민서의 응급 수술
# https://www.acmicpc.net/problem/20955

from sys import stdin

def solution(N, M, edges):

    answer = 0

    # find & union
    parent = [i for i in range(N+1)]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        parent[max(x, y)] = min(x, y)

    for u, v in edges:
        findU, findV = find(u), find(v)
        # 사이클이 존재할 경우
        if findU == findV: answer += 1
        union(findU, findV)

    return answer + sum([1 if parent[i] == i else 0 for i in range(1, N+1)]) - 1

N, M = map(int,stdin.readline().split())
edges = list(list(map(int,stdin.readline().split())) for _ in range(M))

res = solution(N, M, edges)
print(res)