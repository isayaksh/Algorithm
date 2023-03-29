# BOJ 6603 로또
# https://www.acmicpc.net/problem/6603

from sys import stdin
from itertools import combinations

while True:
    order = list(map(int,stdin.readline().split()))
    if len(order) == 1:
        break
    for case in combinations(order[1:], 6):
        print(*case)
    print()