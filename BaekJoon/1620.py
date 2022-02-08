# 1620 나는야 포켓몬 마스터 이다솜 <실버 4>
from sys import stdin

N, M = map(int,stdin.readline().split())
D = {}
for i in range(1,N+1):
  poketmon = stdin.readline().rstrip()
  D[str(i)] = poketmon
  D[poketmon] = str(i)

for _ in range(M):
  key = stdin.readline().rstrip()
  print(D[key])