# BOJ 11568 민균이의 계략
# https://www.acmicpc.net/problem/11568

from sys import stdin

def solution(N, numbers):
    dp = [1] * (N)
    for i in range(1, N):
        for j in range(i):
            if numbers[j] < numbers[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

N = int(stdin.readline())
numbers = list(map(int,stdin.readline().split()))

res = solution(N, numbers)
print(res)