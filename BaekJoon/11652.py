# 11652 카드 <실버 4>
from sys import stdin

N = int(stdin.readline())
D = {}
result = [0, 0] # count, value
for _ in range(N):
  n = int(stdin.readline())
  if n in D:
    D[n] += 1
  else:
    D[n] = 1
  
  if D[n] > result[0]:
    result = [D[n],n]
  elif D[n] == result[0]:
    if n < result[1]:
      result[1] = n
print(result[1])