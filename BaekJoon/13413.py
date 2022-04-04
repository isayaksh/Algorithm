# 13413 오셀로 재배치 < 실버 4 >
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
  N = int(stdin.readline())
  default = stdin.readline().rstrip() # 초기 상태
  target = stdin.readline().rstrip() # 목표 상태
  count = abs(default.count('W') - target.count('W')) # 초기 상태와 목표 상태의 'W' 갯수 차이
  result = count
  for i in range(N):
    if default[i] != target[i]: # 만약 현재 돌의 앞 뒤가 다르다면
      if count <= 0: # 만약 count의 수가 1보다 작다면
        result += 1 # 결과값 + 1
        count += 1 # count + 1
      else:
        count -= 1 # count + 1
  print(result)