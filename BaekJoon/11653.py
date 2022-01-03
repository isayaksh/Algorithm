# 소인수 분해

from sys import stdin
from math import sqrt

N = int(stdin.readline())

count = 2

if N == 1:
  pass
else:
  while N >= count:
    if N%count == 0:
      N//=count
      print(count)
    else: # 2 이외의 모든 소수는 홀수이다!
      if count > 2:
        count+=2
      elif count == 2:
        count+=1