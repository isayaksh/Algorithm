# BOJ 11404 플로이드
# https://www.acmicpc.net/problem/11404

from sys import stdin, maxsize

def solution(n, edges):
    graph = [[maxsize] * n for _ in range(n)]

    # 같은 도시(i → i)로 이동하는 경우
    for i in range(n):
        graph[i][i] = 0
    
    # 버스 비용
    for s, e, w in edges:
        if graph[s-1][e-1] > w:
            graph[s-1][e-1] = w

    # !플로이드 워셜 알고리즘 적용!
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[k][j] > graph[k][i] + graph[i][j]:
                    graph[k][j] = graph[k][i] + graph[i][j]

    # i에서 j로 갈 수 없는 경우
    for y in range(n):
        for x in range(n):
            if graph[y][x] == maxsize:
                graph[y][x] = 0

    return graph

# input
n = int(stdin.readline())
m = int(stdin.readline())
edges = [map(int,stdin.readline().split()) for _ in range(m)]

# req, res
response = solution(n, edges)
for res in response:
    print(*res)