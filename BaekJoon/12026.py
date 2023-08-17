# BOJ 12026 BOJ 거리
# https://www.acmicpc.net/problem/12026

from sys import stdin, maxsize

def solution(N, road):
    dp = [maxsize] * N
    dp[0] = 0

    getPreWord = {'B': 'J', 'O': 'B', 'J': 'O'}
    for i in range(1, N):
        preWord = getPreWord[road[i]]
        for j in range(i):
            if preWord == road[j]:
                dp[i] = min(dp[i], dp[j] + (i-j)**2)
    
    return dp[-1] if dp[-1] != maxsize else -1

N = int(stdin.readline())
road = stdin.readline().strip()

res = solution(N, road)
print(res)