from sys import stdin
N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
count = [1]
for i in range(1,N):
  Min = 1
  for j in range(0,i):
    if A[i] < A[j] and count[j] + 1 > Min :
      Min = count[j] + 1
  count.append(Min)
print(max(count))