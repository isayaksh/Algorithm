# BOJ 2581 소수
# https://www.acmicpc.net/problem/2581

from sys import stdin
from math import sqrt
def solution(N, M):
    primeNumber = [False, False] + [True] * (M-1)

    for i in range(2, int(sqrt(M))+1):
        if primeNumber[i]:
            for j in range(i*2, M+1, i):
                primeNumber[j] = False
    
    primeNumberList = [i for i in range(N, M+1) if primeNumber[i]]
    
    print(-1) if not primeNumberList else print(f'{sum(primeNumberList)}\n{primeNumberList[0]}')

N = int(stdin.readline())
M = int(stdin.readline())

solution(N, M)