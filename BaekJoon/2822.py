# 2822 사과 담기 게임 < 실버 5 >
from sys import stdin
N, M = map(int,stdin.readline().split())
J = int(stdin.readline())
order = [0]
result = 0
for _ in range(J):
  order.append(int(stdin.readline()))
front = 1
for i in range(1,J+1):
  tmp = 0
  if front > order[i]:
    tmp = front - order[i]
    front -= tmp
  if front + (M - 1) < order[i]:
    tmp = order[i] - (front + (M - 1))
    front += tmp
  result += tmp
print(result)