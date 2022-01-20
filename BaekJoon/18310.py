# 18310 안테나 <실버 3>
from sys import stdin

N = int(stdin.readline())
L = list(map(int,stdin.readline().split()))
L.sort()
if N%2:
  print(L[N//2])
else:
  print(L[N//2-1])