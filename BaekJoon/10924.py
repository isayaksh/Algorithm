# BOJ 10924 팰린드롬?
# https://www.acmicpc.net/problem/10942

from sys import stdin

def solution(N, number, M, Q):

    dp = [[False] * (N+1) for _ in range(N+1)]
    for i in range(0, N+1):
        for j in range(1, N+1-i):
            s, e = j, j+i
            if s == e:
                dp[s][e] = True
            elif s+1 == e and number[s] == number[e]:
                dp[s][e] = True
            elif dp[s+1][e-1] and number[s] == number[e]:
                dp[s][e] = True
    
    for d in dp: print(d)
    
    for S, E in Q:
        print(1 if dp[S][E] else 0)

N = int(stdin.readline())
number = [0] + list(map(int,stdin.readline().split()))
M = int(stdin.readline())
Q = list(list(map(int,stdin.readline().split())) for _ in range(M))

solution(N, number, M, Q)