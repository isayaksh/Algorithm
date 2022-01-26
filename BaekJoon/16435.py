# 16435 스네이크버드 <실버 5>
from sys import stdin
N, L = map(int,stdin.readline().split())
H = list(map(int,stdin.readline().split()))

H.sort()
for h in H:
  if L >= h:
    L+=1
  else:
    break
print(L)