# BOJ 21312 홀짝 칵테일
# https://www.acmicpc.net/problem/21312

from sys import stdin

def solution(A, B, C):
    if not A%2 and not B%2 and not C%2:
        return A*B*C
    answer = 1
    for num in (A, B, C):
        if num%2:
            answer *= num
    return answer
A, B, C = map(int,stdin.readline().split())

res = solution(A, B, C)
print(res)