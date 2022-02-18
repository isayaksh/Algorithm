# 19939 박 터뜨리기 <실버 5>
from sys import stdin

N, K = map(int,stdin.readline().split())
tmp = K*(K+1)//2
if N < tmp:
  print(-1)
elif (N-tmp)%K==0:
  print(K-1)
else:
  print(K)