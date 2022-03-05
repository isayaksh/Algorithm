# 13549 숨박꼭질 3 <골드 5>
from collections import deque
from sys import stdin

N, K = map(int,stdin.readline().split())
Count = [-1 for _ in range(100001)] # 현재 위치에 최소한으로 도달하기 위한 횟수 배열
Count[N] = 0
D = deque([N])

while D:
  cur= D.popleft()
  if cur == K:
    print(Count[cur])
    break
  else:
    if cur*2 < 100000 and Count[cur*2] == -1:
      D.appendleft(cur*2)
      Count[cur*2] = Count[cur]
    if cur -1 > -1 and Count[cur-1] == -1:
      D.append(cur-1)
      Count[cur-1] = Count[cur] + 1
    if cur + 1 < 100000 and Count[cur+1] == -1:
      D.append(cur+1)
      Count[cur+1] = Count[cur] + 1