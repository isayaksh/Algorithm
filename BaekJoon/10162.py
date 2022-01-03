from sys import stdin
T = int(stdin.readline())
A = 0
B = 0
if T//300:
  A = T//300
  T -= (T//300)*300
if T//60:
  B = T//60
  T -= (T//60)*60
if T%10:
  print(-1)
else:
  print(A,B,T//10)