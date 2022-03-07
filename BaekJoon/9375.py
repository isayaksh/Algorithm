# 9375 패션왕 신해빈
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
  Dict = {} # 딕셔너리
  result = 1
  n = int(stdin.readline())
  for _ in range(n):
    name, type = stdin.readline().split()
    if type in Dict: # 이미 존재하는 type이면,
      Dict[type] += 1 # +1
    else: # 존재하지 않는 type이면,
      Dict[type] = 1 # 생성
  for d in Dict:
    result *= Dict[d]+1
  print(result-1)