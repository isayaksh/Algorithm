# 2012 등수 매기기 <실버 3>
from sys import stdin

N = int(stdin.readline())
arr = []
result = 0
for _ in range(N):
  arr.append(int(stdin.readline()))
arr.sort()
for i in range(N):
  result += abs((i+1) - arr[i])
print(result)