# BOJ 2309 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

from sys import stdin
from itertools import combinations

def solution(heights):
    for idxs in combinations(range(9), 7):
        sevenDwarf = [heights[idx] for idx in idxs]
        if 100 == sum(sevenDwarf):
            return sevenDwarf

heights = list(sorted(int(stdin.readline()) for _ in range(9)))

res = solution(heights)
for r in res: print(r)