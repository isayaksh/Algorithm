# 진법 변환2

from sys import stdin
from collections import deque

N,B = map(int,stdin.readline().split())

word='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = deque([])

while N!=0:
  result.appendleft(word[N%B])
  N=N//B

print(''.join(result))