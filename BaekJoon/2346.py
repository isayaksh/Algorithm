# 2346 풍선 터뜨리기
from sys import stdin
from collections import deque

N = int(stdin.readline())
O = list(map(int,stdin.readline().split()))
B = deque([i for i in range(1,N+1)])

for _ in range(N):
  count = O[B[0]-1]
  print(B.popleft(),end= " ")
  if not B:
    break
  if count > 0:
    for _ in range(count-1):
      B.append(B.popleft())
  else:
    for _ in range(abs(count)):
      B.appendleft(B.pop())