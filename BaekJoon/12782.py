# 12782 비트 우정지수 < 실버 4 >
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
  N, M = stdin.readline().split()
  ON, OM = N.count('1'), M.count('1') # 비트 지수에 포함된 1의 갯수
  count = 0 # 서로 다른 비트의 갯수
  for i in range(len(N)):
    if N[i] != M[i]:
      count+=1
  count -= abs(ON-OM)
  # 1번 연산 + 2번 연산 + 2번 연산이 끝난 후 남은 비트에 대한 1번 연산
  result = abs(ON-OM) + (count%2) + (count//2) # 
  print(result)