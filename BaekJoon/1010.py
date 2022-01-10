# 1010 다리 놓기 <실버 5>
from sys import stdin
def Combination(N,M):
  result = 1
  N = min(N,M-N)
  for i in range(M-N+1,M+1):
    result *= i
  for i in range(1,N+1):
    result /= i
  print(int(result))
T = int(stdin.readline())
for _ in range(T):
  N, M = map(int,stdin.readline().split())
  Combination(N,M)