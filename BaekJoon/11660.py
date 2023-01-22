# 11660 구간 합 구하기 5 < 실버 1 >
from sys import stdin

# 누적합
def acSum(N, graph):
    for y in range(1,N+1):
        for x in range(2,N+1):
            graph[y][x] += graph[y][x-1]
    for y in range(2,N+1):
        for x in range(1,N+1):
            graph[y][x] += graph[y-1][x]
    return graph

# input
N, M = map(int,stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for y in range(N):
    numbers = list(map(int,stdin.readline().split()))
    for x in range(N):
        graph[y+1][x+1] = numbers[x]

# 그래프 → 누적합 그래프
graph = acSum(N, graph)

for _ in range(M):
    y1, x1, y2, x2 = map(int,stdin.readline().split())
    result = graph[y2][x2] - graph[y2][x1-1] - graph[y1-1][x2] + graph[y1-1][x1-1]
    print(result)
    