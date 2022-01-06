# 2847 게임을 만든 동준이 <실버 4>
from sys import stdin
N = int(stdin.readline())
lst = []
result = 0
for _ in range(N):
  lst.append(int(stdin.readline()))

for i in range(N-1,0,-1):
  if lst[i] <= lst[i-1]:
    tmp = lst[i-1] - lst[i] + 1
    result += tmp
    lst[i-1] -= tmp
print(result)
