from sys import stdin
N = int(stdin.readline())
A = [list(map(int,stdin.readline().split())) for _ in range(N)]
Min = 1001

for i in range(1,N):
  for j in range(3):
    if j == 0:
      A[i][j] = A[i][j] + min(A[i-1][1], A[i-1][2])
    elif j == 1:
      A[i][j] = A[i][j] + min(A[i-1][0], A[i-1][2])
    elif j == 2:
      A[i][j] = A[i][j] + min(A[i-1][0], A[i-1][1])
print(min(A[-1]))