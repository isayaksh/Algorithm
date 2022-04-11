# 11256 사탕 <실버 5>
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
  J, N = map(int,stdin.readline().split())
  lst = []
  count = 0
  for _ in range(N):
    R, C = map(int,stdin.readline().split())
    lst.append(R*C)
  lst.sort(reverse=True)
  for l in lst:
    if J <= 0:
      break
    J -= l
    count += 1
print(count)