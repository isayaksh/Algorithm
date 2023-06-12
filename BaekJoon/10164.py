# BOJ 10164 격자상의 경로
# https://www.acmicpc.net/problem/10164

from sys import stdin

def solution(N, M, K):

    pathGraph = [[0] * 16 for _ in range(16)]
    for i in range(1, 15):
        pathGraph[i][0], pathGraph[0][i] = 1, 1
    
    for y in range(1,16):
        for x in range(1,16):
            pathGraph[y][x] = pathGraph[y-1][x] + pathGraph[y][x-1]

    if K == 0:
        return pathGraph[N-1][M-1]

    return pathGraph[(K-1)//M][(K-1)%M] * pathGraph[(N*M-K)//M][(N*M-K)%M]

N, M, K = map(int,stdin.readline().split())

res = solution(N, M, K)
print(res)