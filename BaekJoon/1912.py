# 연속합

from sys import stdin

n = int(stdin.readline())
dp = list(map(int, stdin.readline().split()))

for i in range(1, n):
  dp[i] = max(dp[i], dp[i - 1] + dp[i])
print(max(dp))