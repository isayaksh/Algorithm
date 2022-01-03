from sys import stdin
T = int(stdin.readline())
for _ in range(T):
  N = int(stdin.readline())
  lst = []
  result = 1
  for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))
  lst.sort()
  MAX = lst[0][1]
  for i in range(1,N):
    if MAX > lst[i][1]:
      result+=1
      MAX = lst[i][1]
  print(result)