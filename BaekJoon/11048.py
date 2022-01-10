# 11048 이동하기 <실버 1>
from sys import stdin
N, M = map(int,stdin.readline().split())
maze = []
for _ in range(N):
  maze.append(list(map(int,stdin.readline().split())))
for i in range(1,N):
  maze[i][0] += maze[i-1][0]
for i in range(1,M):
  maze[0][i] += maze[0][i-1]

for i in range(1,N):
  for j in range(1,M):
    maze[i][j] += max(maze[i-1][j],maze[i][j-1],maze[i-1][j-1])
print(maze[N-1][M-1])