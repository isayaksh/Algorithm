from sys import stdin
N = int(stdin.readline())

A = [0] * (31)
A[2], A[4], A[6] = 3, 11, 41

for i in range(8, 31,2):
  A[i] = A[i-2] * 3 + 2
  for j in range(4, i, 2):
    A[i] += A[i-j] * 2
print(A[N])