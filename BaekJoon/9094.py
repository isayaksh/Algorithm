# BOJ 9094 수학적 호기심
# https://www.acmicpc.net/problem/9094

from sys import stdin

def solution(n, m):
    answer = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a**2+b**2+m)%(a*b) == 0:
                answer += 1
    return answer

T = int(stdin.readline())
for _ in range(T):
    n, m = map(int,stdin.readline().split())
    res = solution(n, m)
    print(res)