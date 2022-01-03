# 가장 긴 증가하는 부분 수열 4

from sys import stdin

A = int(stdin.readline())
Ai = list(map(int,stdin.readline().split()))

result=[1]*A
route = []

for i in range(A):
  tmp = [Ai[i]]
  for j in range(0,i):
    if Ai[i] > Ai[j] and result[i] < result[j]+1:
      result[i] = result[j]+1
      tmp = route[j]+[Ai[i]]
  route.append(tmp)
point = max(result)
print(point)
print(*route[result.index(point)])