# BOJ 15656 N과 M (7)
# https://www.acmicpc.net/problem/15656

from sys import stdin
from itertools import product

def solution(N, M, numbers):
    numbers.sort()
    for res in product(numbers, repeat=M):
        print(*res)

N, M = map(int,stdin.readline().split())
numbers = list(map(int,stdin.readline().split()))

solution(N, M, numbers)