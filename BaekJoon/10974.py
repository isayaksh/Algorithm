# BOJ 10974 모든 순열
# https://www.acmicpc.net/problem/10974

from sys import stdin
from itertools import permutations

def solution(N):
    return [map(str,case) for case in permutations(range(1,N+1), N)]

N = int(stdin.readline())

result = solution(N)
for res in result:
    print(' '.join(res))