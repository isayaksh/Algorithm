# BOJ 2775 부녀회장이 될테야

from sys import stdin

def solution(k, n):
    dp = [[0] * (n+1) for _ in range(k+1)]

    # 0층의 i호에는 i명이 산다.
    for i in range(1,n+1):
        dp[0][i] = i
    
    # 동적 프로그래밍
    for y in range(1,k+1):
        for x in range(1,n+1):
            dp[y][x] = dp[y-1][x] + dp[y][x-1]
    
    return dp[k][n]

T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())
    result = solution(k, n)
    print(result)