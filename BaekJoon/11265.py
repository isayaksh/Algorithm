# BOJ 11265 끝나지 않는 파티
# https://www.acmicpc.net/problem/11265

from sys import stdin

def solution(N, M, graph, order):
    # floyd warshall
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
    # order
    for A, B, C in order:
        print("Enjoy other party") if graph[A-1][B-1] <= C else print("Stay here")

# input
N, M = map(int, stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))
order = list(list(map(int,stdin.readline().split())) for _ in range(M))

solution(N, M, graph, order)