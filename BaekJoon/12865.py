# 12865 평범한 배낭 < 골드 5 >
from sys import stdin
N, K = map(int,stdin.readline().split())
dp = [[0] * (K+1) for _ in range(N+1)]
thing = [[0,0]]
for _ in range(N):
    thing.append(tuple(map(int,stdin.readline().split())))
for i in range(1,N+1):
    for j in range(1,K+1):
        w, v = thing[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[N][K])