# BOJ 18243 Small World Network
# https://www.acmicpc.net/problem/18243

from sys import stdin

def solution(N, K, edges):
    # init graph
    graph = [[0] * (N+1) for _ in range(N+1)]
    for n1, n2 in edges:
        graph[n1][n2] = 1
        graph[n2][n1] = 1
    
    # floyd warshall
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(1,N+1):
                if (graph[j][k] == 0 or graph[j][k] > graph[j][i] + graph[i][k]) and (graph[j][i] != 0 and graph[i][k] != 0):
                    graph[j][k] = graph[j][i] + graph[i][k]

    for y in range(1, N+1):
        for x in range(y+1, N+1):
            if not graph[y][x] or graph[y][x] > 6:
                return "Big World!"
    return "Small World!"

N, K = map(int,stdin.readline().split())
edges = list(list(map(int,stdin.readline().split())) for _ in range(K))

res = solution(N, K, edges)
print(res)