# BOJ 1495 기타리스트
# https://www.acmicpc.net/problem/1495

from sys import stdin

def solution(N, S, M, volumes):
    dp = [[False] * (M+1) for _ in range(N+1)]
    # init
    dp[0][S] = True

    for y in range(1, N+1):
        for x in range(M+1):
            if dp[y-1][x]:
                if x + volumes[y-1] <= M:
                    dp[y][x + volumes[y-1]] = True
                if x - volumes[y-1] >= 0:
                    dp[y][x - volumes[y-1]] = True

    return max([-1] + [i for i in range(M+1) if dp[-1][i]])

N, S, M = map(int,stdin.readline().split())
volumes = list(map(int,stdin.readline().split()))

res = solution(N, S, M, volumes)
print(res)