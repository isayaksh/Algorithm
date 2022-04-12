# 13164 행복 유치원 < 골드 5 >
from sys import stdin
N, K = map(int,stdin.readline().split())
tmp = sorted(list(map(int,stdin.readline().split())))
interval = []
result  =0
for i in range(N-1):
  interval.append(tmp[i+1] - tmp[i])
interval.sort()
for i in range(N-K):
  result += interval[i]
print(result)
