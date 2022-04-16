# 2667 단지 번호 붙이기 <실버 1>
from collections import deque
from sys import stdin

def BFS(x, y):
  D = deque([[x, y]])
  count = 0
  while D:
    [x, y] = D.popleft()
    if x - 1 >= 0 and MAP[y][x-1]: # MAP 범위 내에 아파트가 존재한다면
      D.append([x-1, y]) # 다음 아파트 추가
      MAP[y][x-1] = 0 # 다음 아파트 MAP에서 제거
      count += 1 # 아파트 갯수 추가
    if x + 1 < N and MAP[y][x+1]:
      D.append([x+1, y])
      MAP[y][x+1] = 0
      count += 1
    if y - 1 >= 0 and MAP[y-1][x]:
      D.append([x, y-1])
      MAP[y-1][x] = 0
      count += 1
    if y + 1 < N and MAP[y+1][x]:
      D.append([x, y+1])
      MAP[y+1][x] = 0
      count += 1
  return count # 형성된 단지내 아파트 갯수

N = int(stdin.readline())
MAP = []
answer = []
for _ in range(N):
  MAP.append(list(map(int,stdin.readline().rstrip())))

for x in range(N):
  for y in range(N):
    if MAP[y][x]:
      answer.append(BFS(x,y))
answer.sort()
print(len(answer))
for a in answer:
  print(a)