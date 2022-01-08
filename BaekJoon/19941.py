# 19941 햄버거 분배 <실버 3>
from sys import stdin
def find(result,num,N,K,bench):
  for i in range(num-K,num+K+1):
    if 0 <= i and i < N:
      if bench[i] == 'H':
        result+=1
        bench[i] = None
        break
  return result,bench
N, K = map(int,stdin.readline().split())
bench = list(stdin.readline().rstrip())
result = 0
for i in range(N):
  if bench[i] == "P":
    result, bench = find(result,i,N,K,bench)
print(result)