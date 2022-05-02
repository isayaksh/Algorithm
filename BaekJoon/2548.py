# 2548 대표 자연수 < 실버 3 >
import sys
from sys import stdin
N = int(stdin.readline())
lst = list(map(int,stdin.readline().split()))
lst.sort()
MAX = sys.maxsize
front = 0
back = sum(lst)
for i in range(N):
  back -= lst[i]
  tmp = abs((front - i*lst[i])) + abs((back - (N-i-1)*lst[i]))
  if MAX > tmp:
    MAX, result = tmp, lst[i]
  front += lst[i]
print(result)