# 2812  크게 만들기 < 골드 4 >
from sys import stdin
N,K = map(int,stdin.readline().split())
numbers = list(map(int,stdin.readline().strip()))
result = []
k = K
for i in range(N):
  while k and result and result[-1] < numbers[i]:
    result.pop()
    k-=1
  result.append(numbers[i])
for i in range(N-K):
  print(result[i],end='')