# 2776 암기왕 <실버 4>
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
  D = {}
  N = int(stdin.readline())
  lst = map(int,stdin.readline().split())
  for l in lst:
    D[l] = True
  M = int(stdin.readline())
  lst = map(int,stdin.readline().split())
  for l in lst:
    if l in D:
      print(1)
    else:
      print(0)