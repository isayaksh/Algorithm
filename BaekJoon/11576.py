# Base Conversion

from sys import stdin
from collections import deque

def Base_Conversion(a,A,B):
  decimal = 0
  count = 0
  answer = deque([])
  while a:
    value = a.pop()
    decimal += value*(A**count)
    count+=1
  while decimal:
    answer.appendleft(decimal%B)
    decimal//=B
  print(*answer)

A,B = map(int,stdin.readline().split())
m = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
Base_Conversion(a,A,B)