# 3109 빵집 < 골드 2 >
from sys import stdin
matrix = []
count = 0
DY = [-1,0,1]

def DFS(x, y, R, C):
  if x == C - 1:
    return True
  for dy in DY:
    if y + dy < 0 or y + dy >= R:
      continue
    if matrix[y+dy][x+1] == '.':
      matrix[y+dy][x+1] = 'x'
      if DFS(x+1,y+dy,R,C):
        return True
  return False

R, C = map(int,stdin.readline().split()) # 세로, 가로
for _ in range(R):
  matrix.append(list(stdin.readline().rstrip()))
for i in range(R):
  if matrix[i][0] == '.':
    if DFS(0,i,R,C):
      count += 1
print(count)