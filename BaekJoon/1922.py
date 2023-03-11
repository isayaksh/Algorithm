# BOJ 1922 네트워크 연결
# https://www.acmicpc.net/problem/1922

from sys import stdin


def solution(N, M, edges):
    answer = 0
    edges.sort(key=lambda x : x[2])
    parent = [i for i in range(N+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x = find(x)
        y = find(y)
        parent[max(x,y)] = min(x,y)

    for a, b, c in edges:
        a, b = find(a), find(b)
        if a != b:
            union(a, b)
            answer += c
            N -= 1
            if N == 1:
                break

    return answer

N = int(stdin.readline())
M = int(stdin.readline())
edges = list(list(map(int,stdin.readline().split())) for _ in range(M))

result = solution(N, M, edges)
print(result)