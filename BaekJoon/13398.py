from sys import stdin

n = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
Ap = [A[0]] + [0] * (n-1)
tmp = [A[0]] + [0] * (n-1)
if n == 1:
  print(A[0])
else:
  for i in range(1,n):
    Ap[i] = max(Ap[i-1] + A[i], A[i])
    tmp[i] = max(tmp[i-1] + A[i], Ap[i-1])

  print(max(max(Ap), max(tmp)))