# 11051 이항계수2 <실버 1>
from sys import stdin
N, K = map(int,stdin.readline().split())
value = 1
for i in range(K):
  value  = (value * (N - i) // (i + 1))
print(value%10007)