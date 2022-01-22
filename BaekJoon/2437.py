# 2437 저울 <골드 3>
from sys import stdin

N = int(stdin.readline())
W = list(map(int,stdin.readline().split()))
W.sort()

result = 1
for w in W:
  if result < w:
    break
  result += w
print(result)