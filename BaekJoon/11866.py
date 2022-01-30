# 11866 요세푸스 문제0 <실버 4>
from sys import stdin
from collections import deque
N, K = map(int,stdin.readline().split())
P = deque(i for i in range(1,N+1))
count = 0
print("<",end="")
while count != N:
  for _ in range(K-1):
    P.append(P.popleft())
  print(P.popleft(),end="")
  count+=1
  if count != N:
    print(", ",end="")
  else:
    print(">")