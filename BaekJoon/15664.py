# BOJ 15664 N과 M (10)
# https://www.acmicpc.net/problem/15664

from sys import stdin
from itertools import combinations

def solution(N, M, number):
    number.sort()
    used = set()
    for case in combinations(number, M):
        if case not in used:
            print(*case)
            used.add(case)

N, M = map(int,stdin.readline().split())
number = list(map(int,stdin.readline().split()))

solution(N, M, number)