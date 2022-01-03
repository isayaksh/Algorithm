# -2진수

from sys import stdin
from collections import deque
from math import ceil

def Bn(N):
  result=deque([])
  while N!=0:
    result.appendleft(str(N%2))
    N = ceil(N/-2)
  return result

N = int(stdin.readline())

if N == 0:
  print(0)
elif N == 1:
  print(1)
else:
  result = ''.join(Bn(N))
  print(result)