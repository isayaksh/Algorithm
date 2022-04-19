# 1012 유기농 배추 < 실버 2 >
from collections import deque
from sys import stdin

def DFS(x,y):
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  D = deque([[x,y]])
  while D:
    [x, y] = D.popleft()
    for i in range(4):
      curX = x + dx[i]
      curY = y + dy[i]
      if  curX < 0 or curX > M-1 or curY < 0 or curY > N-1:
        continue
      if field[curY][curX]:
        D.append([curX,curY])
        field[curY][curX] = 0

T = int(stdin.readline())
result = []
for _ in range(T):
  M, N, K = map(int,stdin.readline().split()) # 가로, 세로, 배추 갯수
  field = [[0 for _ in range(M)] for _ in range(N)]
  for _ in range(K):
    x, y = map(int,stdin.readline().split())
    field[y][x] = 1
  count = 0
  for y in range(N):
    for x in range(M):
      if field[y][x]: # 현재 위치에 배추가 존재한다면
        count += 1 # 지렁이 갯수 + 1
        DFS(x,y) # DFS
  result.append(count)
for c in result:
  print(c)