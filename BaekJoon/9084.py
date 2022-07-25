# 9084 동전 < 골드 5 >
from sys import stdin

def func(coins,M):
    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(1,M+1):
            # 현재 금액에서 동전 값을 뺀 가격이 0보다 크다면
            if i - coin >= 0: 
                # 현재 금액의 위치에 현재 금액에서 동전 값을 뺀 가격에 위치한 금액을 만드는 방법의 수를 더한다.
                dp[i] += dp[i-coin] 
    return dp[M]

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    coins = list(map(int,stdin.readline().split()))
    M = int(stdin.readline())
    print(func(coins,M))