# 14501 퇴사 <실버 3>
from sys import stdin

N = int(stdin.readline())
TP = [[0,0]]
for _ in range(N):
  TP.append(list(map(int,stdin.readline().split())))
maxSum = [0 for _ in range(N+1)]
for i in range(N,0,-1):
  if TP[i][0] - 1 +  i  <= N:
    tmp = 0
    for j in range(TP[i][0]+i,N+1):
      if maxSum[j] > tmp:
        tmp = maxSum[j]
    maxSum[i] = TP[i][1] + tmp
print(max(maxSum))