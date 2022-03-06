# 1697 숨바꼭질 <실버 1>
from collections import deque
from sys import stdin

MAX = 100001
N, K = map(int,stdin.readline().split())
Count = [0 for _ in range(MAX)]
Deque = deque([N])

while Deque:
  cur = Deque.popleft()
  if cur == K:
    print(Count[cur])
    break
  if cur + 1 < MAX and Count[cur + 1] == 0:
    Deque.append(cur + 1)
    Count[cur+1] = Count[cur] + 1
  if cur - 1 > -1 and Count[cur - 1] == 0:
    Deque.append(cur - 1)
    Count[cur-1] = Count[cur] + 1
  if cur * 2 < MAX and Count[cur*2] == 0:
    Deque.append(cur * 2)
    Count[cur*2] = Count[cur] + 1