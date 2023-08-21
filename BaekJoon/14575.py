# BOJ 14575 뒤풀이
# https://www.acmicpc.net/problem/14575

from sys import stdin, maxsize

def solution(N, T, drinkLevel):

    def function(target):
        minT, maxT = 0, 0
        for L, R in drinkLevel:
            if target < L: return False
            minT += L
            maxT += target if target < R else R
        if minT <= T <= maxT:
            return True

    for target in range(1, 10**6+1):
        if function(target):
            return target
    
    return -1

N, T = map(int,stdin.readline().split())
drinkLevel = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, T, drinkLevel)
print(res)