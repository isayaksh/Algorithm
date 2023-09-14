# BOJ 1912 연속합
# https://www.acmicpc.net/problem/1912

from sys import stdin

def solution(n, numbers):
    dp = [numbers[0]] + [0] * (n-1)
    for i in range(1, n):
        dp[i] = numbers[i] + dp[i-1] if numbers[i] < numbers[i] + dp[i-1] else numbers[i]
    return max(dp)

n = int(stdin.readline())
numbers = list(map(int,stdin.readline().split()))

res = solution(n, numbers)
print(res)