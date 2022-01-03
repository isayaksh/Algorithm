# 가장 긴 증가하는 부분 수열

from sys import stdin

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

result=[1]*N

for i in range(1,N):
  for j in range(0,i):
    if A[i] > A[j] and result[j]+1 > result[i]:
      result[i] = result[j]+1
print(max(result))