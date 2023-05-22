# BOJ 4948 베르트랑 공준
# https://www.acmicpc.net/problem/4948

from sys import stdin
from math import sqrt
from bisect import bisect

# 에라토스테네스의 체
NUM = 246912
primeNumber = set(i for i in range(2, NUM+1))
for i in range(2, int(sqrt(NUM))):
    if i in primeNumber:
        for j in range(i*2, NUM+1, i):
            primeNumber.discard(j)
primeNumber = list(sorted(primeNumber))

while True:
    n = int(stdin.readline())
    if n == 0: break
    # 이진탐색
    print(bisect(primeNumber, n*2) - bisect(primeNumber, n))