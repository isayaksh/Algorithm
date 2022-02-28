# 1904 01 타일 < 실버 3>
from sys import stdin
N = int(stdin.readline())
pre1 = 1 # N -2 번째 항
pre2 = 2 # N- 1 번째 항
if N == 1:
  print(1)
elif N == 2:
  print(2)
else:
  for i in range(3,N+1):
    cur = (pre1 + pre2) % 15746 # lst[N] = lst[N-1] + lst[N-2]
    pre1 = pre2 % 15746
    pre2 = cur % 15746
  print(cur)