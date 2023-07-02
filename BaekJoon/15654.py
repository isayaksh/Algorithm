# BOJ 15654 N과 M (5)
# https://www.acmicpc.net/problem/15654

from sys import stdin
from itertools import permutations

def solution(N, M, numbers):
    numbers.sort()
    for case in permutations(numbers, M):
        print(*case)

N, M = map(int,stdin.readline().split())
numbers = list(map(int,stdin.readline().split()))

solution(N, M, numbers)