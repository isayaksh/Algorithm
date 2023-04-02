# BOJ 1644 소수의 연속합
# https://www.acmicpc.net/problem/1644

from sys import stdin
from math import sqrt

def solution(N):
    answer = 0
    
    # 에라토스테네스의 체
    primeNumber = [False, False] + [True] * (N-1)
    for i in range(2, int(sqrt(N))+1):
        if primeNumber[i]:
            for j in range(2*i, N+1, i):
                primeNumber[j] = False
    primeNumber = [0] + [i for i in range(2, N+1) if primeNumber[i]]

    # 누적합
    n = len(primeNumber)
    for i in range(1, n):
        primeNumber[i] += primeNumber[i-1]

    # 이분 탐색
    start, end = 0, 1
    while end < n:
        total = primeNumber[end] - primeNumber[start]
        if total == N:
            answer += 1
            end += 1
        elif total < N:
            end += 1
        else:
            start += 1

    return answer

# input
N = int(stdin.readline())

# result
print(solution(N))