# 9009 피보나치 <실버 1>
from sys import stdin
from collections import deque
T = int(stdin.readline())
lst = []
for _ in range(T):
  lst.append(int(stdin.readline()))
M = max(lst)
fib = deque([1,0])
while True:
  tmp = fib[0] + fib[1]
  if tmp > M:
    break
  else:
    fib.appendleft(tmp)
for num in lst:
  result = deque([])
  for j in fib:
    if num >= j and num:
      result.appendleft(str(j))
      num -= j
  print(" ".join(result))