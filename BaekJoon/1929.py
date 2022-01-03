# 소수 구하기

from sys import stdin
import math

M,N=map(int,stdin.readline().split())

def Prime_number(n):
  if n < 2:
    return False
  error = True
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      error=False
      break
  return error

for i in range(M,N+1):
  if Prime_number(i):
    print(i)