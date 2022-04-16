# 2178 미로 탐색 < 실버 1 >
from collections import deque
from sys import stdin

N, M = map(int,stdin.readline().split())
maze = []
for _ in range(N):
  tmp = list(map(int,stdin.readline().rstrip()))
  for i in range(M):
    if tmp[i] == 1: tmp[i] = 10001 # 이동할 수 있는 칸의 값을 1에서 10001으로 변경
  maze.append(tmp)
D =  deque([[0, 0, 1]])

answer = 0
while D:
  [x, y, count] = D.popleft() # [ x좌표, y좌표, 이동 횟수 ]
  #  미로의 범위내 and 이동할 수 있는 칸 and 이동 횟수가 현재 이동할 칸의 값보다 작을 때
  if x - 1 >= 0 and maze[y][x-1] != 0 and maze[y][x-1] > count+1:
    D.append([x-1,y,count+1]) # BFS에 이동할 칸 추가
    maze[y][x-1] = count + 1 # 이동할 칸에 이동 횟수 입력
  if x + 1 < M and maze[y][x+1] != 0 and maze[y][x+1] > count +1:
    D.append([x+1,y,count+1])
    maze[y][x+1] = count + 1
  if y - 1 >= 0 and maze[y-1][x] != 0 and maze[y-1][x] > count +1:
    D.append([x,y-1,count+1])
    maze[y-1][x] = count + 1
  if y + 1 < N and maze[y+1][x] != 0 and maze[y+1][x] > count +1 :
    D.append([x,y+1,count+1])
    maze[y+1][x] = count + 1
print(maze[N-1][M-1]) # 도착지점의 이동횟수 값 출력