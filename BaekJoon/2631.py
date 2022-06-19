# 2631 줄세우기 <골드 4>
from sys import stdin
from bisect import bisect_left
N = int(stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(stdin.readline()))
lis = [lst[0]]
for i in range(N):
    if lst[i] > lis[-1]: lis.append(lst[i])
    else: lis[bisect_left(lis, lst[i])] = lst[i]
print(N-len(lis))