# 1, 2, 3 더하기 5

from sys import stdin

A = [[0,0,0],[1,0,0],[0,1,0],[1,1,1]]

for i in range(4,100001):
  A.append([A[i-1][1]+A[i-1][2],A[i-2][0]+A[i-2][2],A[i-3][0]+A[i-3][1]])
  # 리스트에 계속해서 큰 값이 입력되면
  # 자료가 너무 커져서 처리하는데 시간이 오래걸림
  A[i][0]%=1000000009
  A[i][1]%=1000000009
  A[i][2]%=1000000009

T = int(stdin.readline())

for _ in range(T):
  n = int(stdin.readline())
  print(sum(A[n])%1000000009)