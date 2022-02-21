# 9461 파도반 수열<실버 3>
from sys import stdin
result = [0,1,1,1]
for i in range(4,101):
  result.append(result[i-2]+result[i-3])
T = int(stdin.readline())
for _ in range(T):
  n = int(stdin.readline())
  print(result[n])