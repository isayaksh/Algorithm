# BOJ 11170 0의 개수 
# https://www.acmicpc.net/problem/11170

from sys import stdin

dp = [1] + [0] * 1000000
for i in range(1, 1000001):
    dp[i] = dp[i-1] + str(i).count('0')

for _ in range(int(stdin.readline())):
    N, M = map(int,stdin.readline().split())
    print(dp[M] - (dp[N-1] if N != 0 else 0))