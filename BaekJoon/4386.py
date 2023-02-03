# BOJ 4386 별자리 만들기
# https://www.acmicpc.net/problem/4386

from sys import stdin
from math import sqrt

def solution(n, dots):

    answer = 0

    # UNION & FIND
    parent = [i for i in range(n+1)]
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        parent[max(x, y)] = min(x, y)

    distances = []
    # 2개의 별(dot1, dot2) 사이의 거리를 반환
    def distance(dot1, dot2):
        return sqrt(abs(dot1[0] - dot2[0])**2 + abs(dot1[1] - dot2[1])**2)
    # 모든 별 사이의 거리를 계산
    for y in range(n):
        for x in range(n):
            if x == y: continue
            # (별 사이의 거리, 별1, 별2)
            distances.append((distance(dots[x], dots[y]), x, y))
    # 별 사이의 거리를 기준으로 오름차순으로 정렬
    distances.sort()

    # Kruskal MST 알고리즘
    for dist, x, y in distances:
        x, y = find(x), find(y)
        # 2개의 별(x, y)이 연결되어 있지 않다면
        if x != y:
            # 현재 거리 연결
            answer += dist
            union(x, y)

    return answer

n = int(stdin.readline())
dots = [list(map(float,stdin.readline().split())) for _ in range(n)]

res = solution(n, dots)
print(res)