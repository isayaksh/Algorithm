# 5430 AC <골드 5>
from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
  P = stdin.readline().rstrip()
  n = int(stdin.readline())
  X = deque(stdin.readline().strip("[ ] \n").split(","))
  
  if n == 0:
    X = deque([])

  R = True # Reverse
  TF = True 

  for p in P:
    if p == 'R':
      R = not R
    elif p == 'D':
      if X:
        if R:
          X.popleft()
        else:
          X.pop()
      else:
        print("error")
        TF= False
        break
  if TF:
    if not R:
      X.reverse()      
    print("[{}]".format(",".join(X)))




