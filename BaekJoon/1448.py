# 1448 삼각형 만들기 <실버 3>
from sys import stdin
N = int(stdin.readline())
lst = []
for _ in range(N):
  lst.append(int(stdin.readline()))
lst.sort()
for i in range(N-1,1,-1):
  if lst[i] < lst[i-1] + lst[i-2]:
    print(lst[i] + lst[i-1] + lst[i-2])
    exit()
print(-1)