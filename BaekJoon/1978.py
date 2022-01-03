# 소수 찾기

from sys import stdin
import math
N = int(stdin.readline())
NN = map(int,stdin.readline().split())

count = 0

for n in NN:
  error = False
  if n > 1:
    for i in range(2,int(math.sqrt(n))+1):
      if n%i==0:
        error=True
        break
    if not error:
      count+=1
print(count)