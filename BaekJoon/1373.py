# 2진수 8진수

from sys import stdin
import collections

def Transform(I):
  result=0
  count=1
  for i in I:
    result+=int(i)*count
    count*=2
  return str(result)

I = list(stdin.readline().rstrip())

L= len(I)

if L%3==0:
  L//=3
else:
  L = L//3+1
result = collections.deque([])

for i in range(L):
  temp=collections.deque([])
  while I:
    if len(temp) > 2:
      break
    temp.append(I.pop())
  result.appendleft(Transform(temp))

result = "".join(result)

print(result)