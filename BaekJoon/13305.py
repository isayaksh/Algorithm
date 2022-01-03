from sys import stdin
N = int(stdin.readline())
K = list(map(int,stdin.readline().split()))
C = list(map(int,stdin.readline().split()))
MIN = C[0]
LEN = 0
SUM = K[0] * C[0]
for i in range(1,N-1):
  if MIN < C[i]:
    LEN += K[i]
  else:
    SUM += MIN * LEN
    MIN = C[i]
    LEN = K[i]
SUM += MIN * LEN
print(SUM)