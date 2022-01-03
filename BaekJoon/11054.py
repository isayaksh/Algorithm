from sys import stdin
N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

forward = [1] * N
reverse = [1] * N
bito = [0] * N

for i in range(1,N):
  for j in range(0,i):
    if A[i] > A[j] and forward[j] + 1 > forward[i]:
      forward[i] = forward[j] + 1

A.reverse()

for i in range(1,N):
  for j in range(0,i):
    if A[i] > A[j] and reverse[j] + 1 > reverse[i]:
      reverse[i] = reverse[j] + 1

for i in range(N):
  bito[i] = forward[i] + reverse[N-i-1] - 1

print(max(bito))