from sys import stdin
N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
tmp = [A[0]]
for i in range(1,N):
  Max = A[i]
  for j in range(0,i):
    if A[i] > A[j] and A[i] + tmp[j] > Max:
      Max = A[i] + tmp[j]
  tmp.append(Max)
print(max(tmp))