# 14425 문자열 집합 < 실버 3>
from sys import stdin
N, M = map(int,stdin.readline().split())
S = set()
count = 0
for _ in range(N):
 S.add(stdin.readline().rstrip())
for _ in range(M):
  if stdin.readline().rstrip() in S:
    count += 1
print(count)