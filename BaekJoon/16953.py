from sys import stdin
from collections import deque
A, B = map(int,stdin.readline().split())
D = deque([[B,1]])
while D:
  tmp = D.popleft()
  if tmp[0] == A:
    print(tmp[1])
    exit()
  if tmp[0] % 10 == 1:
    D.append([tmp[0] // 10, tmp[1]+1])
  if tmp[0] % 2 == 0 and tmp[0] != 0:
    D.append([tmp[0] // 2, tmp[1]+1])
print(-1)