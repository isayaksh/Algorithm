# BOJ 13707 합분해 2
# https://www.acmicpc.net/problem/13707

from sys import stdin

def solution(N, K):

    dp = [[0] * (N+1) for _ in range(K+1)]
    dp[1] = [1] * (N+1)
    for y in range(K+1):
        dp[y][0] = 1
    
    for y in range(2, K+1):
        for x in range(1, N+1):
            dp[y][x] = (dp[y][x-1] + dp[y-1][x]) % 1000000000

    return dp[K][N]

N, K = map(int,stdin.readline().split())

res = solution(N, K)
print(res)