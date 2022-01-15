# 2262 토너먼트 만들기
from sys import stdin, maxsize

n = int(stdin.readline())
R = list(map(int,stdin.readline().split()))
result = 0
while n > 1:
  idx = R.index(max(R))
  if idx == 0:
    result += abs(R[idx]-R[idx+1])
  elif idx == n-1:
    result += abs(R[idx]-R[idx-1])
  else:
    result += min(abs(R[idx]-R[idx+1]),abs(R[idx]-R[idx-1]))
  del R[idx]
  n-=1
print(result)