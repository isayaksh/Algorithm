# BOJ 3040 백설 공주와 일곱 난쟁이
# https://www.acmicpc.net/problem/3040

from sys import stdin
from itertools import combinations

def solution(dwarf):
    for sevenDwarf in combinations(dwarf, 7):
        if sum(sevenDwarf) == 100:
            return sevenDwarf

# input
dwarf = list(int(stdin.readline()) for _ in range(9))

# result
res = solution(dwarf)
print(*res, sep='\n')