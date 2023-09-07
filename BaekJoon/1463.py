# BOJ 1463 1로 만들기
# https://www.acmicpc.net/problem/1463

from sys import stdin, maxsize

def solution(X):
    dp = [maxsize] * (X+1)
    dp[1] = 0

    for i in range(1, X):
        # [1] X가 3으로 나누어 떨어지면, 3으로 나눈다.
        if i * 3 <= X and dp[i*3] > dp[i] + 1:
            dp[i*3] = dp[i] + 1

        # [2] X가 2로 나누어 떨어지면, 2로 나눈다.
        if i * 2 <= X and dp[i*2] > dp[i] + 1:
            dp[i*2] = dp[i] + 1

        # [3] 1을 뺀다.
        if i + 1 <= X and dp[i+1] > dp[i] + 1:
            dp[i+1] = dp[i] + 1

    return dp[X] 

X = int(stdin.readline())

res = solution(X)
print(res)