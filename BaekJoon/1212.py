# 8진수 2진수

from sys import stdin
from collections import deque

N = deque(list(stdin.readline().rstrip()))

if N[0]=='0':
  print(0)
else:
  result = deque([])

  while N:
    C = int(N.popleft())
    count = 4
    while count>=1:
      if C >= count:
        C-=count
        result.append('1')
      else:
        result.append('0')
      count//=2
  while 1:
    if result[0]=='0':
      result.popleft()
    else:
      break
  
  result = ''.join(result)
  print(result)




