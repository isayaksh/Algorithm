# 골드바흐의 추측

from sys import stdin
import math

def Prime_number(n):
  error = True
  for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
      error=False
      break
  return error

while(1):
  error=False
  n = int(stdin.readline())
  if n == 0:
    break
  for i in range(3,1000000,2):
    if Prime_number(i) and Prime_number(n-i):
      print("{} = {} + {}".format(n,i,n-i))
      break