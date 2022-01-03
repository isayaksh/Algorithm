# 쉬운 계단 수

from sys import stdin

A = [[0,1,1,1,1,1,1,1,1,1]]

for i in range(99):
  result=[A[i][1]]
  for j in range(1,9):
    result.append((A[i][j-1]+A[i][j+1])%1000000000)
  result.append(A[i][8])
  A.append(result)

N = int(stdin.readline())

print(sum(A[N-1])%1000000000)