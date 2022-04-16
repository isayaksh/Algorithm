# 1260  DFS와 BFS
from sys import stdin
from collections import deque

def DFS(v, visited):
  print(v, end=" ")
  visited[v] = False
  for i in arr[v]:
    if visited[i]:
      DFS(i,visited)

def BFS(v, visited):
  visited[v] = False
  D = deque([v])
  while D:
    tmp = D.popleft()
    print(tmp,end=" ")
    for i in arr[tmp]:
      if visited[i]:
        visited[i] = False
        D.append(i)
  print()

# main()
N, M, V = map(int,stdin.readline().split())
arr = [ [0 for _ in range(N+1)] for _ in range(N+1) ]
for _ in range(M):
  x, y = map(int,stdin.readline().split())
  arr[x][y] = y
  arr[y][x] = x

visited = [False]+[True for _ in range(N)]
DFS(V, visited)
print()
visited = [False]+[True for _ in range(N)]
BFS(V, visited)