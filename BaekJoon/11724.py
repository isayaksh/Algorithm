# 11724 연결 요소의 개수
from collections import deque
from sys import stdin

N, M = map(int,stdin.readline().split())
matrix = [[] for _ in range(N+1)] # 연결 노드
visited = [True for _ in range(N+1)] # 방문한 노드
count = 0 # 요소의 개수
for _ in range(M):
  x, y = map(int,stdin.readline().split())
  matrix[y].append(x)
  matrix[x].append(y)

# BFS
for i in range(1,N+1): 
  if visited[i]:
    count += 1
    D = deque(matrix[i])
    while D:
      tmp = D.popleft()
      if visited[tmp]:
        visited[tmp] = False
        D += matrix[tmp]
print(count)