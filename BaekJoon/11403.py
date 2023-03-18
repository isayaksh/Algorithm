# BOJ 11403 경로 찾기
# https://www.acmicpc.net/problem/11403

from sys import stdin

def solution(N, graph):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][i] == 1 and graph[i][k] == 1:
                    graph[j][k] = 1
    return graph

# input
N = int(stdin.readline())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

# result
result = solution(N, graph)
for res in result:
    print(*res)