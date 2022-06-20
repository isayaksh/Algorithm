# 14469 소가 길을 건너간 이유 3 < 실버 4 >
from re import T
from sys import stdin

N = int(stdin.readline())
lst = []
for _ in range(N):
    lst.append(tuple(map(int,stdin.readline().split())))
lst.sort()
time = 0
for a, t in lst:
    if time < a: time = a
    time += t
    print(time)
print(time)
