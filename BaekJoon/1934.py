# 최소 공배수

from sys import stdin

N = int(stdin.readline())

for i in range(N):
  A,B = map(int,stdin.readline().split())
  if A==0 or B==0:
    print(0)
  else:
    C = A*B
    while B:
      A,B = B,A%B
    print(C//A)