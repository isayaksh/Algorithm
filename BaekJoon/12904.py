# 12904 A와 B <골드 5>
from sys import stdin

S = list(stdin.readline().rstrip())
T = list(stdin.readline().rstrip())

num = len(T) - len(S)

for _ in range(num):
  if T[-1] == 'A':
    T.pop()
  else:
    T.pop()
    T.reverse()

if "".join(T) == "".join(S):
  print(1)
else:
  print(0)