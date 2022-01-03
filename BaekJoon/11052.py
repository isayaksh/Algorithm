# 카드 구매하기

from sys import stdin

N = int(stdin.readline())
P = [0]+list(map(int,stdin.readline().split()))
A=[0,P[1]]

for i in range(2,N+1):
  max = P[i]
  for j in range(1,i//2+1):
    if max < A[j]+A[i-j]:
      max = A[j]+A[i-j]
  A.append(max)
print(A[-1])