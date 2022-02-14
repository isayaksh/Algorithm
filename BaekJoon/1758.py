# 1758 알바생 강호 <실버 4>
from sys import stdin

N = int(stdin.readline())

O = []
result = 0

for _ in range(N):
  O.append(int(stdin.readline()))
O.sort(reverse=True)

for i in range(N):
  if O[i] - i > 0:
    result += O[i] - i
print(result)