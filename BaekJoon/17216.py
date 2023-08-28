# BOJ 17216 가장 큰 감소 부분 수열
# https://www.acmicpc.net/problem/17216

from sys import stdin

def solution(N, A):
    dp = [a for a in A]
    for i in range(1,N):
        for j in range(i):
            if A[i] < A[j]:
                dp[i] = max(dp[i], A[i] + dp[j])
    return max(dp)

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

res = solution(N, A)
print(res)