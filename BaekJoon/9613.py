# GCD 합

from sys import stdin

def GCD(A,B):
  while B!=0:
    A,B=B,A%B
  return A


t = int(stdin.readline())
for i in range(t):
  n = list(map(int,stdin.readline().split()))
  result=0
  for i in range(1,n[0]):
    for j in range(i+1,n[0]+1):
      if n[i]>n[j]:
        result+=GCD(n[i],n[j])
      else:
        result+=GCD(n[j],n[i])
  print(result)
