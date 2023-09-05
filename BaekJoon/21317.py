# BOJ 21317 징검다리 건너기
# https://www.acmicpc.net/problem/21317

from sys import stdin, maxsize
from collections import deque

def solution(N, jump, K):

    dp = [[maxsize] * (N+1) for _ in range(N+1)]
    for i in range(N-1):
        dp[i][i+1] = min(dp[i][i+1], jump[i][0])
        dp[i][i+2] = min(dp[i][i+2], jump[i][1])

    for i in range(N):
        for j in range(N):
            for k in range(N):
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

    for y in range(N):
        for x in range(N):
            if dp[y][x] == maxsize:
                dp[y][x] = 0

    answer = dp[0][N-1]

    for i in range(N-3):
        answer = min(answer, dp[0][i] + K + dp[i+3][N-1])
    return answer

N = int(stdin.readline())
jump = list(list(map(int,stdin.readline().split())) for _ in range(N-1))
K = int(stdin.readline())

res = solution(N, jump, K)
print(res)