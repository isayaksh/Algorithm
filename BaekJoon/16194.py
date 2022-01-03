# 카드 구매하기 2

from sys import stdin

N = int(stdin.readline())
P = [0]+list(map(int,stdin.readline().split()))

A = [0,P[1]]

for i in range(2,N+1):
  M = P[i]
  for j in range(1,i//2+1):
    if M > A[i-j] + A[j]:
      M = A[i-j] + A[j]
  A.append(M)
print(A[-1])