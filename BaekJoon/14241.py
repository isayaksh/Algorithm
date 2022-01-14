# 14241 슬라임 합치기 <실버2>
from sys import stdin
N = int(stdin.readline())
S = list(map(int,stdin.readline().split()))
S.sort()
result = 0
for _ in range(N-1):
  s1 = S.pop()
  s2 = S.pop()
  result += s1*s2
  S.append(s1+s2)
print(result)