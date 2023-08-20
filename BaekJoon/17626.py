# BOJ 17626 Four Squares
# https://www.acmicpc.net/problem/17626

from sys import stdin, maxsize
from math import sqrt

def solution(n):
    dp = [maxsize] * (n+1)
    for i in range(1, int(sqrt(n))+1):
        dp[i**2] = 1

    for i in range(2, n+1):
        if dp[i] != maxsize: continue
        for j in range(1, int(sqrt(i))+1):
            if dp[i] > dp[i-j**2]+1:
                dp[i] = dp[i-j**2]+1
    
    return dp[n]

res = solution(int(stdin.readline()))
print(res)