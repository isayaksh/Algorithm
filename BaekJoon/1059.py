# BOJ 1059 좋은 구간
# https://www.acmicpc.net/problem/1059

from sys import stdin

def solution(L, S, n):
    S.sort()
    for i in range(L):
        if S[i] < n < S[i+1]:
            return (n - (S[i]+1)) * (S[i+1] - n) + (S[i+1] - n - 1)
    return 0

L = int(stdin.readline())
S = [0] + list(map(int,stdin.readline().split()))
n = int(stdin.readline())

res = solution(L, S, n)
print(res)
