# 12852 1로 만들기 2 < 실버 1 >
from sys import stdin
N = int(stdin.readline())
dp = [[] for _ in range(N+1)]
dp[1] = [1]
for i in range(1,N+1):
    if dp[i] == []: continue
    num = len(dp[i])
    if i*3 <= N:
        if dp[i*3] == [] or num < len(dp[i*3]): dp[i*3] = [i*3] + dp[i]
    if i*2 <= N:
        if dp[i*2] == [] or num < len(dp[i*2]): dp[i*2] = [i*2] + dp[i]
    if i+1 <= N:
        if dp[i+1] == [] or num < len(dp[i+1]): dp[i+1] = [i+1] + dp[i]
print(len(dp[N]) - 1)
for number in dp[N]:
    print(number,end=" ")