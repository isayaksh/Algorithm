# 1764 듣보잡 <실버 4>
from sys import stdin
N, M = map(int,stdin.readline().split())
A = set(stdin.readline().rstrip() for _ in range(N))
B = set(stdin.readline().rstrip() for _ in range(M))

result = list(A&B) # 입력받은 값들의 교집합
result.sort()
print(len(result))
for r in result:
  print(r)