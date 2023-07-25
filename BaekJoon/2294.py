# BOJ 2294 동전 2
# https://www.acmicpc.net/problem/2294

from sys import stdin, maxsize

def solution(n, k, coins):
    dp = [0] + [maxsize] * k
    for i in range(1, k+1):
        for coin in coins:
            if 0 <= i-coin and dp[i] > dp[i-coin] + 1:
                dp[i] = dp[i-coin] + 1
    return dp[k] if dp[k] != maxsize else -1

n, k = map(int,stdin.readline().split())
coins = set(int(stdin.readline()) for _ in range(n))

res = solution(n, k, coins)
print(res)