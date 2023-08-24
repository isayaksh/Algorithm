# BOJ 22864 피로도
# https://www.acmicpc.net/problem/22864

from sys import stdin

def solution(A, B, C, M):
    answer = 0
    fatigue = 0

    for _ in range(24):
        if fatigue + A > M:
            fatigue = max(0, fatigue - C)
        else:
            answer += B
            fatigue += A

    return answer

A, B, C, M = map(int,stdin.readline().split())

res = solution(A, B, C, M)
print(res)