# 2*n 타일링 2

from sys import stdin

n = int(stdin.readline())

a,b=1,3

if n < 3:
  print(n*2-1)
else:
  for i in range(n-2):
    a,b=b,a*2+b
  print(b%10007)