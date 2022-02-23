# 5397 키로커 <실버 3>
from sys import stdin
from collections import deque

def pw(S):
  front = []
  back = deque([])
  for s in S:
    if s == "<":
      if  front:
        back.appendleft(front.pop())
    elif s == ">":
      if back:
        front.append(back.popleft())
    elif s == "-":
      if front:
        front.pop()
    else:
      front.append(s)
  print("".join(front)+"".join(back))
T = int(stdin.readline())
for _ in range(T):
  S = stdin.readline().rstrip()
  pw(S)