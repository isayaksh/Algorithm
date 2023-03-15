# BOJ 1038 감소하는 수
# https://www.acmicpc.net/problem/1038

from sys import stdin
from itertools import combinations

decreasingNumber = []
for i in range(1,11):
    for number in combinations(range(10), i):
        decreasingNumber.append(int(''.join(list(map(str,reversed(number))))))
decreasingNumber.sort()

N = int(stdin.readline())
try:
    print(decreasingNumber[N])
except:
    print(-1)