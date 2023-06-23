# BOJ 17212 달나라 토끼를 위한 구매대금 지불 도우미
# https://www.acmicpc.net/problem/17212

from sys import stdin

def solution(N):
    dp = [0, 1, 1, 2, 2, 1, 2, 1] + [0] * (N-7)
    for i in range(8, N+1):
        dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1
    return dp[N]

# input
N = int(stdin.readline())

# response
res = solution(N)
print(res)