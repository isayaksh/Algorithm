# 7785 회사에 있는 사람
from sys import stdin
D = {}
n = int(stdin.readline())
for _ in range(n):
  name, el= stdin.readline().rstrip().split(" ")
  if el == "enter":
    D[name] = 0
  else:
    del D[name]

result = list(D.keys())
result.sort(reverse=True)
for name in result:
  print(name,end=' ')