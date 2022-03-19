# 10546 배부른 마라토너 < 실버 4 >
from sys import stdin
N = int(stdin.readline())
Dict = {}
for i in range(N):
  name = stdin.readline().strip()
  if name in Dict:
    Dict[name] += 1
  else:
    Dict[name] = 1
for _ in range(N-1):
  name = stdin.readline().strip()
  Dict[name] -= 1
print(Dict)
for name in Dict:
  if Dict[name]:
    print(name)
    break