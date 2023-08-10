# BOJ 16195 1, 2, 3 더하기 9
# https://www.acmicpc.net/problem/16195

from sys import stdin
from collections import defaultdict

dp = [dict(), {1: 1}, {1: 1, 2: 1}, {1: 1, 2: 2, 3: 1}]
for i in range(4, 1001):
    tmp = defaultdict(int)
    for j in range(i-3, i):
        for key in dp[j]:
            tmp[key+1] += dp[j][key]
    dp.append(tmp)

def solution(n, m):
    count = 0
    for key in dp[n]:
        if key > m: break
        count += dp[n][key]
    return count

for _ in range(int(stdin.readline())):
    n, m = map(int,stdin.readline().split())
    res = solution(n, m)
    print(res%1000000009)